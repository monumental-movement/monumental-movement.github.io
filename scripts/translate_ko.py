import os
import yaml
import re
import json
from deep_translator import GoogleTranslator
from concurrent.futures import ThreadPoolExecutor, as_completed

# ---------------------------------------------
# CONFIG
# ---------------------------------------------
SRC_DIR = "_posts"
DEST_DIR = os.path.join("ko", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='ko')
CACHE_FILE = "translation_cache.json"

# ---------------------------------------------
# LOAD / SAVE CACHE
# ---------------------------------------------
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        CACHE = json.load(f)
else:
    CACHE = {}

def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(CACHE, f, ensure_ascii=False, indent=2)

# ---------------------------------------------
# EXCLUDE BLOCKS (残したい)
# ---------------------------------------------
EXCLUDE_BLOCK_PATTERNS = [
    (r"<style[\s\S]*?</style>", "STYLE"),
    (r"<script[\s\S]*?</script>", "SCRIPT"),
    (r"<table[\s\S]*?</table>", "TABLE"),
    (r"<div class=\"mermaid\"[\s\S]*?</div>", "MERMAID"),
    (r"```[\s\S]*?```", "CODEBLOCK"),
]

def extract_excluded_blocks(text):
    placeholders = {}
    idx = 0
    for pattern, tag in EXCLUDE_BLOCK_PATTERNS:
        for m in re.finditer(pattern, text):
            block = m.group(0)
            ph = f"__EXCLUDE_{tag}_{idx}__"
            placeholders[ph] = block
            text = text.replace(block, ph)
            idx += 1
    return text, placeholders

def restore_excluded_blocks(text, placeholders):
    for ph, block in placeholders.items():
        text = text.replace(ph, block)
    return text

# ---------------------------------------------
# TRANSLATE WITH CACHE
# ---------------------------------------------
def translate_text(text):
    if text in CACHE:
        return CACHE[text]
    try:
        result = translator.translate(text)
        CACHE[text] = result
        return result
    except Exception:
        return text

# ---------------------------------------------
# MERMAID TRANSLATION
# ---------------------------------------------
def translate_mermaid_line(line):
    # %% コメント
    line = re.sub(r'%%\s*(.*)', lambda m: '%% ' + translate_text(m.group(1)), line)

    # ノードラベル
    patterns = [
        (r'(\[)(.*?)(\])'),
        (r'(\()([^()]*)(\))'),
        (r'(\(\()([^()]*)(\)\))'),
        (r'(\|)(.*?)(\|)'),
    ]
    for pat in patterns:
        def repl(m):
            start, text, end = m.group(1), m.group(2), m.group(3)
            # 日本語文字が含まれる場合だけ翻訳
            if re.search(r'[一-龯ぁ-んァ-ン]', text):
                return f"{start}{translate_text(text)}{end}"
            return m.group(0)
        line = re.sub(pat, repl, line)
    return line

# ---------------------------------------------
# YAML HANDLING
# ---------------------------------------------
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content

def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except:
        return {}

def extract_slug(filename):
    base = os.path.splitext(filename)[0]
    base = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', base)
    slug = re.sub(r'[^\w]+', '-', base)
    return slug.lower().strip('-')

# ---------------------------------------------
# TRANSLATE ARTICLE
# ---------------------------------------------
def translate_article(filename):
    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    tmp, placeholders = extract_excluded_blocks(content)
    fm, body = split_front_matter(tmp)
    fm_dict = load_yaml_safe(fm)

    # title
    if fm_dict.get("title"):
        fm_dict["title"] = translate_text(fm_dict["title"])

    slug = extract_slug(filename)
    fm_dict["lang"] = "ko"
    fm_dict["permalink"] = f"/ko/{slug}/"

    # body
    translated_body = ""
    in_mermaid_block = False

    for line in body.splitlines():
        if line.strip().startswith(("graph", "flowchart")):
            in_mermaid_block = True
            translated_body += line + "\n"
            continue
        if in_mermaid_block:
            if line.strip() == "":
                translated_body += line + "\n"
                continue
            translated_body += translate_mermaid_line(line) + "\n"
            if line.strip() == "</div>":
                in_mermaid_block = False
            continue
        # 通常行
        translated_body += translate_text(line) + "\n"

    final = f"---\n{yaml.safe_dump(fm_dict, allow_unicode=True)}---\n{translated_body}"
    final = restore_excluded_blocks(final, placeholders)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final)

    return filename

# ---------------------------------------------
# MAIN
# ---------------------------------------------
files = [f for f in os.listdir(SRC_DIR) if f.endswith(".md")]

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(translate_article, f) for f in files]
    for future in as_completed(futures):
        print("✅ Done:", future.result())

save_cache()
print("\n🎉 Korean translation completed with cache & parallelization + Mermaid translation!")
