import os
import yaml
import re
import json
import time
import signal
from deep_translator import GoogleTranslator
from difflib import unified_diff

# =========================================================
# 設定
# =========================================================
SRC_DIR = "_posts"
DEST_DIR = os.path.join("de", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source="ja", target="de")

CACHE_FILE = "translation_cache_de.json"
MAX_LEN = 600
SLEEP_SEC = 0.6
TIMEOUT_SEC = 30

# =========================================================
# キャッシュ
# =========================================================
TRANSLATION_CACHE = {}
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        TRANSLATION_CACHE = json.load(f)

def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(TRANSLATION_CACHE, f, ensure_ascii=False, indent=2)

# =========================================================
# タイムアウト（Unix系）
# =========================================================
class Timeout(Exception):
    pass

def handler(signum, frame):
    raise Timeout()

signal.signal(signal.SIGALRM, handler)

# =========================================================
# ユーティリティ
# =========================================================
def contains_ja(text):
    return len(re.findall(r"[一-龯ぁ-んァ-ン]", text)) >= 3

def chunk_text(text, max_len=MAX_LEN):
    chunks, buf = [], ""
    for line in text.splitlines(keepends=True):
        if len(buf) + len(line) > max_len:
            chunks.append(buf)
            buf = line
        else:
            buf += line
    if buf:
        chunks.append(buf)
    return chunks

# =========================================================
# 翻訳（耐久版）
# =========================================================
def translate_text(text):
    if not isinstance(text, str):
        text = str(text)

    if text in TRANSLATION_CACHE:
        return TRANSLATION_CACHE[text]

    try:
        signal.alarm(TIMEOUT_SEC)
        time.sleep(SLEEP_SEC)
        translated = translator.translate(text)
        signal.alarm(0)

        if not translated:
            translated = text

        TRANSLATION_CACHE[text] = translated
        return translated

    except Exception:
        signal.alarm(0)
        TRANSLATION_CACHE[text] = text
        return text

def safe_translate(text):
    return "".join(translate_text(c) for c in chunk_text(text))

# =========================================================
# 翻訳除外ブロック
# =========================================================
EXCLUDE_BLOCK_PATTERNS = [
    (r"<style[\s\S]*?</style>", "STYLE"),
    (r"<script[\s\S]*?</script>", "SCRIPT"),
    (r"<table[\s\S]*?</table>", "TABLE"),
    (r"<div class=\"mermaid\"[\s\S]*?</div>", "MERMAID"),
]

def extract_excluded_blocks(text):
    placeholders, idx = {}, 0
    for pattern, tag in EXCLUDE_BLOCK_PATTERNS:
        for m in list(re.finditer(pattern, text)):
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

# =========================================================
# 本文翻訳
# =========================================================
def translate_paragraphs(text):
    result = []
    for p in text.split("\n\n"):
        if contains_ja(p):
            result.append(safe_translate(p))
        else:
            result.append(p)
    return "\n\n".join(result)

def process_body(body):
    segments = re.split(r"(<div class=\"mermaid\"[\s\S]*?</div>)", body)
    out = []
    for seg in segments:
        if seg.startswith('<div class="mermaid"'):
            out.append(seg)
        else:
            out.append(translate_paragraphs(seg))
    return "".join(out)

# =========================================================
# YAML / slug
# =========================================================
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content

def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except Exception:
        return {}

def extract_slug(filename):
    base = os.path.splitext(filename)[0]
    base = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", base)
    return re.sub(r"[^\w]+", "-", base).lower().strip("-")

# =========================================================
# メイン
# =========================================================
for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    print(f"\n📄 Processing: {filename}")

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src = f.read()

    cleaned, placeholders = extract_excluded_blocks(src)
    fm, body = split_front_matter(cleaned)
    front_matter = load_yaml_safe(fm)

    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            old = f.read()
        _, old_body = split_front_matter(old)
        if not list(unified_diff(old_body.splitlines(), body.splitlines())):
            print("⏭️ No changes → Skip")
            continue

    if front_matter.get("title"):
        front_matter["title"] = safe_translate(front_matter["title"])

    slug = extract_slug(filename)
    front_matter["lang"] = "de"
    front_matter["permalink"] = f"/de/{slug}/"

    new_body = process_body(body)

    final = restore_excluded_blocks(
        f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{new_body}",
        placeholders
    )

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final)

    save_cache()
    print("🇩🇪✅ Done")

print("\n🎉 Free & Stable German translation finished!")
