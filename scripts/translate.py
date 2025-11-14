import os
import yaml
import re
from deep_translator import GoogleTranslator
from difflib import unified_diff

SRC_DIR = "_posts"
DEST_DIR = os.path.join("en", "_posts")
CACHE_FILE = "translation_cache.yaml"

os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='en')

# ----------------------------------------
#  キャッシュ読み込み
# ----------------------------------------
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        translation_cache = yaml.safe_load(f) or {}
else:
    translation_cache = {}

def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(translation_cache, f, allow_unicode=True)

# ----------------------------------------
# 引用符の正規化
# ----------------------------------------
def normalize_quotes(text):
    return re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)

# ----------------------------------------
# 翻訳 + 段落キャッシュ
# ----------------------------------------
def translate_paragraph(text):
    stripped = text.strip()
    if not stripped:
        return text  # 空行はそのまま

    # コード/iframeは翻訳しない
    if stripped.startswith("```") or "<iframe" in stripped:
        return text

    # キャッシュ利用
    if stripped in translation_cache:
        return translation_cache[stripped]

    try:
        result = translator.translate(stripped)
        if result is None:
            result = stripped
        result = normalize_quotes(result)
    except Exception as e:
        print(f"⚠️ Translate failed → {e}")
        result = stripped

    translation_cache[stripped] = result
    return result

# ----------------------------------------
# Front matter を分離
# ----------------------------------------
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content

# ----------------------------------------
# 本文の翻訳（段落ごと）
# ----------------------------------------
def translate_body(body):
    out = []
    in_code = False

    for line in body.splitlines(True):  # 改行維持
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code = not in_code
            out.append(line)
            continue

        if in_code or "<iframe" in stripped:
            out.append(line)
            continue

        # --- 本文の段落処理（全文をまとめて翻訳 → 高精度） ---
        if stripped:
            translated = translate_paragraph(line)
            out.append(translated + ("\n" if not line.endswith("\n") else ""))
        else:
            out.append(line)

    return "".join(out)

# ----------------------------------------
# メイン処理
# ----------------------------------------
for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    fm, body = split_front_matter(src_content)
    front = yaml.safe_load(fm) or {}

    # 既存ファイルあり → 差分チェック（高速化）
    old_body = ""
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            old_content = f.read()
        _, old_body = split_front_matter(old_content)

    if old_body.strip() == body.strip():
        print(f"⏭️ No changes: {filename}")
        continue

    print(f"🔁 Updating: {filename}")

    # --- YAML title 翻訳 ---
    if front.get("title"):
        front["title"] = translate_paragraph(front["title"])

    front["lang"] = "en"

    # --- 本文翻訳 ---
    translated_body = translate_body(body)

    # --- 書き出し ---
    output = f"---\n{yaml.safe_dump(front, allow_unicode=True)}---\n{translated_body}"

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ Done: {filename}\n")

# 最後にキャッシュ保存
save_cache()
print("🎉 Finished translation (with paragraph cache)")
