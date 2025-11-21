import os
import re
import yaml
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from deep_translator import GoogleTranslator

# ---------------------------------------------
# CONFIG
# ---------------------------------------------
WORKSPACE = os.getcwd()  # GitHub Actionsでも安全
SRC_DIR = os.path.join(WORKSPACE, "_posts")
DEST_DIR = os.path.join(WORKSPACE, "ko", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

CACHE_FILE = os.path.join(WORKSPACE, "translation_cache_ko.json")
MAX_WORKERS = 8

translator = GoogleTranslator(source='ja', target='ko')

# ---------------------------------------------
# キャッシュ読み込み
# ---------------------------------------------
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        TRANSLATION_CACHE = json.load(f)
else:
    TRANSLATION_CACHE = {}

# ---------------------------------------------
# EXCLUDE BLOCK PATTERNS
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
# 翻訳ラッパー（キャッシュ付き・None安全）
# ---------------------------------------------
def cached_translate(text: str) -> str:
    if not text.strip():
        return text
    key = hashlib.md5(text.encode("utf-8")).hexdigest()
    if key in TRANSLATION_CACHE:
        return TRANSLATION_CACHE[key] or text
    try:
        translated = translator.translate(text)
        if not translated:
            translated = text
        TRANSLATION_CACHE[key] = translated
        return translated
    except Exception:
        return text

# ---------------------------------------------
# Mermaid ノード・コメント翻訳
# ---------------------------------------------
def translate_mermaid_line(line):
    def repl_comment(m):
        return "%% " + cached_translate(m.group(1))
    line = re.sub(r"%%\s*(.*)", repl_comment, line)

    patterns = [
        (r'(\[)(.*?)(\])'),
        (r'(\()([^()]*)(\))'),
        (r'(\(\()([^()]*)(\)\))'),
        (r'(\|)(.*?)(\|)'),
    ]
    for pat in patterns:
        def repl(m):
            start, text, end = m.group(1), m.group(2), m.group(3)
            if re.search(r'[一-龯ぁ-んァ-ン]', text):
                return f"{start}{cached_translate(text)}{end}"
            return m.group(0)
        line = re.sub(pat, repl, line)
    return line

# ---------------------------------------------
# YAML / Slug
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
# 個別記事翻訳
# ---------------------------------------------
def translate_article(filename):
    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    tmp, placeholders = extract_excluded_blocks(content)
    fm, body = split_front_matter(tmp)
    fm_dict = load_yaml_safe(fm)

    if fm_dict.get("title"):
        fm_dict["title"] = cached_translate(fm_dict["title"])
    slug = extract_slug(filename)
    fm_dict["lang"] = "ko"
    fm_dict["permalink"] = f"/ko/{slug}/"

    translated_lines = []
    in_code = False
    in_mermaid = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            translated_lines.append(line)
            continue
        if in_code:
            translated_lines.append(line)
            continue
        if line.strip().startswith("graph") or line.strip().startswith("flowchart"):
            in_mermaid = True
            translated_lines.append(line)
            continue
        if in_mermaid:
            if line.strip() in ("", "</div>", "</div>"):
                if line.strip().lower() == "</div>":
                    in_mermaid = False
                translated_lines.append(line)
                continue
            translated_lines.append(translate_mermaid_line(line))
            continue
        translated_lines.append(cached_translate(line))

    final_content = f"---\n{yaml.safe_dump(fm_dict, allow_unicode=True)}---\n" + "\n".join(translated_lines)
    final_content = restore_excluded_blocks(final_content, placeholders)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_content)

    print("✅ Translated:", filename)
    return filename

# ---------------------------------------------
# 並列実行
# ---------------------------------------------
md_files = [f for f in os.listdir(SRC_DIR) if f.endswith(".md")]
print(f"🔄 Translating {len(md_files)} articles with {MAX_WORKERS} threads...")

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {executor.submit(translate_article, f): f for f in md_files}
    for future in as_completed(futures):
        try:
            future.result()
        except Exception as e:
            print("❌ Error:", futures[future], e)

# ---------------------------------------------
# キャッシュ保存
# ---------------------------------------------
with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(TRANSLATION_CACHE, f, ensure_ascii=False, indent=2)

print("\n🎉 All Korean translations completed!")
