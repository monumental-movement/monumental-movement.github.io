import os
import yaml
import re
import time
from deep_translator import GoogleTranslator

# ==== 基本設定 ====
SRC_DIR = "_posts"                     # 日本語記事
DEST_DIR = os.path.join("pages", "en", "_posts")  # ✅ 出力先
CACHE_FILE = "translation_cache.yaml"
MAX_RUNTIME = 6 * 60 * 60        # 6時間（秒）
SAFE_EXIT_MARGIN = 10 * 60       # 終了10分前に安全終了
AUTO_SAVE_INTERVAL = 50          # 翻訳50件ごとにキャッシュ保存
BATCH_SIZE = 50                  # バッチ翻訳単位

os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='en')
start_time = time.time()
translate_count = 0

# ==== キャッシュ管理 ====
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(cache, f, allow_unicode=True)

cache = load_cache()

# ==== 正規化 ====
def normalize_quotes(text):
    if not text:
        return text
    return re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)

# ==== 翻訳関数（バッチ対応） ====
def translate_batch(paragraphs):
    """50段落まとめて翻訳"""
    global translate_count, cache

    to_translate = []
    keys = []
    translated = []

    for p in paragraphs:
        key = p.strip()
        if not key or key.startswith("```") or re.search(r'<iframe.*?</iframe>', key, re.DOTALL) or key.startswith("<!--"):
            translated.append(p)
            continue
        if key in cache:
            translated.append(cache[key])
            continue
        to_translate.append(key)
        keys.append(key)
        translated.append(None)

    if not to_translate:
        return translated

    elapsed = time.time() - start_time
    if elapsed > (MAX_RUNTIME - SAFE_EXIT_MARGIN):
        print("⏳ Runtime approaching 6 hours — safe exit triggered.")
        save_cache(cache)
        exit(0)

    try:
        text_block = "\n\n".join(to_translate)
        result_block = translator.translate(text_block)
        result_paragraphs = [normalize_quotes(t.strip()) for t in result_block.split("\n\n")]

        for k, r in zip(keys, result_paragraphs):
            cache[k] = r
            translate_count += 1
            if translate_count % AUTO_SAVE_INTERVAL == 0:
                save_cache(cache)
                print(f"💾 Cache auto-saved ({translate_count} translations)")

        idx = 0
        for i, val in enumerate(translated):
            if val is None:
                translated[i] = result_paragraphs[idx]
                idx += 1

    except Exception as e:
        print("⚠️ Batch translation failed:", e)
        for i, val in enumerate(translated):
            if val is None:
                translated[i] = paragraphs[i]

    return translated

def translate_paragraphs(paragraphs):
    result = []
    for i in range(0, len(paragraphs), BATCH_SIZE):
        batch = paragraphs[i:i+BATCH_SIZE]
        result.extend(translate_batch(batch))
        time.sleep(0.05)
    return result

# ==== Front Matter ====
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content

def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except yaml.YAMLError:
        return {}

# ==== メイン処理 ====
try:
    for filename in os.listdir(SRC_DIR):
        if not filename.endswith(".md"):
            continue

        src_path = os.path.join(SRC_DIR, filename)
        dest_path = os.path.join(DEST_DIR, filename)

        with open(src_path, "r", encoding="utf-8") as f:
            src_content = f.read()

        fm, body = split_front_matter(src_content)
        front_matter = load_yaml_safe(fm)

        old_body = ""
        if os.path.exists(dest_path):
            with open(dest_path, "r", encoding="utf-8") as f:
                dest_content = f.read()
            fm2, old_body = split_front_matter(dest_content)

        old_paragraphs = re.split(r'\n\s*\n', old_body)
        new_paragraphs = re.split(r'\n\s*\n', body)

        if old_paragraphs == new_paragraphs and old_body.strip():
            print(f"⏭️ No changes: {filename}")
            continue
        elif old_body.strip():
            print(f"🔁 Diff detected: {filename} — {len([p for p in new_paragraphs if p not in old_paragraphs])} paragraphs changed")
        else:
            print(f"🆕 New file: {filename} — 全文翻訳")

        translated_paragraphs = translate_paragraphs(new_paragraphs)
        translated_body = "\n\n".join(translated_paragraphs)

        if front_matter.get("title"):
            front_matter["title"] = translate_paragraphs([front_matter["title"]])[0]

        front_matter["lang"] = "en"

        output_content = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}\n"
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(output_content)

        print(f"✅ Translated/Updated: {filename}")

finally:
    save_cache(cache)
    print("\n💾 Final cache saved. All progress preserved safely.")
    print("🎉 English posts updated successfully (→ pages/en/_posts, 6h-safe, cached, diff-based).")
