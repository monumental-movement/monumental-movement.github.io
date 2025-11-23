import os
import yaml
import re
import time
import json
import hashlib
import concurrent.futures
from deep_translator import GoogleTranslator

# -------------------------------
# 設定
# -------------------------------
SRC_DIR = "_posts"
DEST_DIR = os.path.join("ko", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

CACHE_FILE = "translation_cache_ko.json"
MAX_WORKERS = 4

translator = GoogleTranslator(source='ja', target='ko')

# キャッシュ読み込み
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        TRANSLATION_CACHE = json.load(f)
else:
    TRANSLATION_CACHE = {}

# -------------------------------
# 翻訳除外ブロック
# -------------------------------
EXCLUDE_BLOCK_PATTERNS = [
    (r"<style[\s\S]*?</style>", "STYLE"),
    (r"<script[\s\S]*?</script>", "SCRIPT"),
    (r"<table[\s\S]*?</table>", "TABLE"),
    (r"<iframe[\s\S]*?</iframe>", "IFRAME"),
    (r"<div class=\"mermaid\"[\s\S]*?</div>", "MERMAID"),
    (r"```[\w]*[\s\S]*?```", "CODEBLOCK"),
]

def extract_excluded_blocks(text):
    placeholders = {}
    idx = 0
    for pattern, tag in EXCLUDE_BLOCK_PATTERNS:
        for m in re.finditer(pattern, text, re.MULTILINE):
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

# -------------------------------
# 短文ごとに翻訳（キャッシュ＋リトライ）
# -------------------------------
SPLIT_PATTERN = re.compile(r'(?<=[。！？\n])')  # 句点・改行で分割

def cached_translate(text, retries=3):
    text = str(text).strip()
    if not text:
        return text
    key = hashlib.md5(text.encode("utf-8")).hexdigest()
    if key in TRANSLATION_CACHE:
        return TRANSLATION_CACHE[key]

    # 短文分割して翻訳
    parts = SPLIT_PATTERN.split(text)
    translated_parts = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        for _ in range(retries):
            try:
                result = translator.translate(part)
                if result:
                    translated_parts.append(result)
                    break
            except Exception:
                time.sleep(0.3)
        else:
            translated_parts.append(part)
    translated_text = "".join(translated_parts)
    TRANSLATION_CACHE[key] = translated_text
    return translated_text

# -------------------------------
# Mermaidノード／コメント翻訳
# -------------------------------
def translate_mermaid_line(line):
    line = re.sub(r"%%\s*(.*)", lambda m: "%% " + cached_translate(m.group(1)), line)
    patterns = [
        (r'(\[)(.*?)(\])'),
        (r'(\()([^()]*)(\))'),
        (r'(\(\()([^()]*)(\)\))'),
        (r'(\|)(.*?)(\|)'),
    ]
    for pattern in patterns:
        def repl(m):
            start, text, end = m.group(1), m.group(2), m.group(3)
            return f"{start}{cached_translate(text)}{end}"
        line = re.sub(pattern, repl, line)
    return line

# -------------------------------
# YAML / slug
# -------------------------------
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split('---', 2)
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

# -------------------------------
# 記事翻訳
# -------------------------------
def process_article(filename):
    if not filename.endswith(".md"):
        return
    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    cleaned, placeholders = extract_excluded_blocks(content)
    fm, body = split_front_matter(cleaned)
    fm_dict = load_yaml_safe(fm)

    if "title" in fm_dict:
        fm_dict["title"] = cached_translate(fm_dict["title"])

    slug = extract_slug(filename)
    fm_dict["lang"] = "ko"
    fm_dict["permalink"] = f"/ko/{slug}/"

    translated_lines = []
    in_code = False
    in_mermaid = False

    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            translated_lines.append(line)
            continue
        if in_code:
            translated_lines.append(line)
            continue
        if stripped.startswith("graph") or stripped.startswith("flowchart"):
            in_mermaid = True
            translated_lines.append(line)
            continue
        if in_mermaid:
            if stripped == "</div>":
                in_mermaid = False
                translated_lines.append(line)
            else:
                translated_lines.append(translate_mermaid_line(line))
            continue
        # 本文短文分割翻訳
        translated_lines.append(cached_translate(line))

    final = restore_excluded_blocks(
        f"---\n{yaml.safe_dump(fm_dict, allow_unicode=True)}---\n" + "\n".join(translated_lines),
        placeholders
    )

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final)

    print(f"✅ {filename} translated")

# -------------------------------
# 並列処理
# -------------------------------
if __name__ == "__main__":
    files = [f for f in os.listdir(SRC_DIR) if f.endswith(".md")]
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        list(executor.map(process_article, files))

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(TRANSLATION_CACHE, f, ensure_ascii=False, indent=2)

    print("\n🎉 All Korean translations completed! No Japanese left.")
