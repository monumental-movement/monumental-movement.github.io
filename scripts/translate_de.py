import os
import yaml
import re
import json
import time
from deep_translator import GoogleTranslator
from difflib import unified_diff
from concurrent.futures import ThreadPoolExecutor, TimeoutError

# =========================================================
# 設定
# =========================================================
SRC_DIR = "_posts"
DEST_DIR = os.path.join("de", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source="ja", target="de")

CACHE_FILE = "translation_cache_de.json"

MAX_LEN = 500           # 1チャンク最大文字数
SLEEP_SEC = 0.7         # Google対策（必須）
TRANSLATE_TIMEOUT = 20  # 1翻訳の最大秒数
MAX_FILES = 3           # 1回の実行で処理する最大記事数

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
# ユーティリティ
# =========================================================
def contains_ja(text):
    return len(re.findall(r"[一-龯ぁ-んァ-ン]", text)) >= 3

def looks_translated(text):
    return re.search(r"[äöüß]", text) is not None

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
# 翻訳（Windows対応・強制タイムアウト）
# =========================================================
def _translate_call(text):
    return translator.translate(text)

def translate_with_timeout(text):
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(_translate_call, text)
        try:
            return future.result(timeout=TRANSLATE_TIMEOUT)
        except TimeoutError:
            return text
        except Exception:
            return text

def translate_text(text):
    if not isinstance(text, str):
        text = str(text)

    if text in TRANSLATION_CACHE:
        return TRANSLATION_CACHE[text]

    time.sleep(SLEEP_SEC)

    translated = translate_with_timeout(text)
    if not translated:
        translated = text

    TRANSLATION_CACHE[text] = translated
    return translated

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
    out = []
    for p in text.split("\n\n"):
        if looks_translated(p):
            out.append(p)
        elif contains_ja(p):
            out.append(safe_translate(p))
        else:
            out.append(p)
    return "\n\n".join(out)

def process_body(body):
    segments = re.split(r"(<div class=\"mermaid\"[\s\S]*?</div>)", body)
    result = []
    for seg in segments:
        if seg.startswith('<div class="mermaid"'):
            result.append(seg)
        else:
            result.append(translate_paragraphs(seg))
    return "".join(result)

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
count = 0

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

    count += 1
    if count >= MAX_FILES:
        print("🛑 Rate protection stop (Windows safe)")
        break

print("\n🎉 Windows-safe free translation finished!")
