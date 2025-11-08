import os
import yaml
import re
import time
from deep_translator import GoogleTranslator
from difflib import unified_diff

SRC_DIR = "_posts"
DEST_DIR = os.path.join("en", "_posts")
CACHE_FILE = "translation_cache.yaml"
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='en')

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
translate_count = 0


# ==== 正規化 ====
def normalize_quotes(text):
    if not text:
        return text
    text = re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)
    return text


# ==== 高速翻訳（キャッシュ対応・段落単位） ====
def translate_paragraphs(paragraphs):
    global translate_count
    translated = []
    for p in paragraphs:
        key = p.strip()
        if not key or re.match(r"^```", key) or re.search(r'<iframe.*?</iframe>', key, re.DOTALL):
            translated.append(p)
            continue

        if key in cache:
            translated.append(cache[key])
            continue

        try:
            # バッチ翻訳
            result = translator.translate(key)
            result = normalize_quotes(str(result))
            cache[key] = result
            translated.append(result)
            translate_count += 1

            if translate_count % 100 == 0:
                save_cache(cache)
                print(f"💾 Cache auto-saved ({translate_count})")

        except Exception as e:
            print(f"⚠️ 翻訳失敗: {e} — {key[:40]}")
            translated.append(p)
            continue

        time.sleep(0.05)  # 軽めの遅延
    return translated


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


# ==== メイン ====
for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    fm, body = split_front_matter(src_content)
    front_matter = load_yaml_safe(fm)

    # 差分検出
    old_body = ""
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            dest_content = f.read()
        fm2, old_body = split_front_matter(dest_content)

    if old_body.strip():
        diff = list(unified_diff(old_body.splitlines(), body.splitlines()))
        if not diff:
            print(f"⏭️ No changes: {filename}")
            continue
        else:
            print(f"🔁 Diff detected: {filename} — 高速差分翻訳")
    else:
        print(f"🆕 New file: {filename} — 全文高速翻訳")

    # 段落単位で翻訳（空行で分割）
    paragraphs = re.split(r'\n\s*\n', body)
    translated_paragraphs = translate_paragraphs(paragraphs)
    translated_body = "\n\n".join(translated_paragraphs)

    # タイトル翻訳
    if front_matter.get("title"):
        front_matter["title"] = translate_paragraphs([front_matter["title"]])[0]

    front_matter["lang"] = "en"

    # 出力
    output_content = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}\n"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"✅ Translated/Updated: {filename}")

# ==== 終了処理 ====
save_cache(cache)
print("\n🎉 English posts updated successfully (cached, fast, diff-based)")
