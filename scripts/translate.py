import os
import yaml
import re
import time
from deep_translator import GoogleTranslator

# =========================================
# 基本設定
# =========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
SRC_DIR = os.path.join(ROOT_DIR, "_posts")         # 日本語記事
DEST_DIR = os.path.join(ROOT_DIR, "en", "_posts")  # 英語記事
CACHE_FILE = os.path.join(ROOT_DIR, "translation_cache.yaml")

MAX_RUNTIME = 6 * 60 * 60        # 最大6時間
SAFE_EXIT_MARGIN = 10 * 60       # 終了10分前で安全終了
AUTO_SAVE_INTERVAL = 50          # 50件ごとにキャッシュ自動保存
BATCH_SIZE = 20                  # GoogleTranslator は小さめバッチが安定

os.makedirs(DEST_DIR, exist_ok=True)
translator = GoogleTranslator(source="ja", target="en")

start_time = time.time()
translate_count = 0

# =========================================
# キャッシュ管理
# =========================================
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(cache, f, allow_unicode=True)

cache = load_cache()

# =========================================
# 正規化（翻訳ノイズ除去）
# =========================================
def normalize_quotes(text):
    if not text:
        return text
    return re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)

# =========================================
# 翻訳バッチ処理
# =========================================
def translate_batch(paragraphs):
    """キャッシュ付きで GoogleTranslator による高速翻訳"""
    global translate_count, cache

    to_translate, keys, translated = [], [], []

    for p in paragraphs:
        key = p.strip()
        # 翻訳不要な要素
        if (
            not key
            or key.startswith("```")
            or key.startswith("<!--")
            or "<iframe" in key
        ):
            translated.append(p)
            continue

        # キャッシュ使用
        if key in cache:
            translated.append(cache[key])
            continue

        to_translate.append(key)
        keys.append(key)
        translated.append(None)

    if not to_translate:
        return translated

    # 制限時間チェック
    if time.time() - start_time > (MAX_RUNTIME - SAFE_EXIT_MARGIN):
        print("⏳ Safe exit: time limit approaching.")
        save_cache(cache)
        exit(0)

    try:
        # GoogleTranslatorは文書全体より小ブロックの方が安定
        text_block = "\n\n".join(to_translate)
        result_block = translator.translate(text_block)
        result_paragraphs = [
            normalize_quotes(t.strip()) for t in result_block.split("\n\n") if t.strip()
        ]

        for k, r in zip(keys, result_paragraphs):
            cache[k] = r
            translate_count += 1
            if translate_count % AUTO_SAVE_INTERVAL == 0:
                save_cache(cache)
                print(f"💾 Cache auto-saved ({translate_count})")

        idx = 0
        for i, val in enumerate(translated):
            if val is None:
                if idx < len(result_paragraphs):
                    translated[i] = result_paragraphs[idx]
                    idx += 1
                else:
                    translated[i] = to_translate[idx - 1]  # fallback

    except Exception as e:
        print(f"⚠️ Batch translation failed: {e}")
        for i, val in enumerate(translated):
            if val is None:
                translated[i] = paragraphs[i]

    return translated


def translate_paragraphs(paragraphs):
    result = []
    for i in range(0, len(paragraphs), BATCH_SIZE):
        batch = paragraphs[i : i + BATCH_SIZE]
        result.extend(translate_batch(batch))
        time.sleep(0.02)  # 負荷軽減のための最小スリープ
    return result


# =========================================
# Front Matter処理
# =========================================
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content


def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except yaml.YAMLError:
        return {}


# =========================================
# メイン処理
# =========================================
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
            _, old_body = split_front_matter(dest_content)

        old_paragraphs = re.split(r"\n\s*\n", old_body)
        new_paragraphs = re.split(r"\n\s*\n", body)

        # 差分チェック
        #if old_paragraphs == new_paragraphs and old_body.strip():
        #    print(f"⏭️ No changes: {filename}")
        #    continue
        #elif old_body.strip():
        #    print(f"🔁 Diff detected: {filename}")
        #else:
        #    print(f"🆕 New file: {filename}")

        # 翻訳
        translated_paragraphs = translate_paragraphs(new_paragraphs)
        translated_body = "\n\n".join(translated_paragraphs)

        # タイトル翻訳
        if front_matter.get("title"):
            front_matter["title"] = translate_paragraphs([front_matter["title"]])[0]

        # 言語設定
        front_matter["lang"] = "en"

        output_content = (
            "---\n"
            + yaml.safe_dump(front_matter, allow_unicode=True, sort_keys=False)
            + "---\n"
            + translated_body
            + "\n"
        )

        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(output_content)

        print(f"✅ Translated/Updated: {filename}")

finally:
    save_cache(cache)
    print("\n💾 Final cache saved. All progress preserved safely.")
    print("🎉 English posts updated successfully (→ en/_posts, diff-based, cached).")
