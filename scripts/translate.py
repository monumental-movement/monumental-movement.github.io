import os
import yaml
import re
import time
from googletrans import Translator

# 翻訳元・翻訳先ディレクトリ
SRC_DIR = "_posts"
DEST_DIR = os.path.join("en", "_posts")

# 出力ディレクトリが無ければ作成
os.makedirs(DEST_DIR, exist_ok=True)

translator = Translator()

# === 引用符統一 ===
def normalize_quotes(text):
    if not text:
        return text
    text = re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)
    text = re.sub(r'``(.*?)``', r'"\1"', text)
    text = re.sub(r"''(.*?)''", r'"\1"', text)
    text = re.sub(r"\b'(.*?)'\b", r'"\1"', text)
    return text

# === 翻訳処理（リトライ付き） ===
def translate_text(text, retries=3):
    if not text.strip():
        return text
    if re.search(r'<iframe.*?</iframe>', text, re.DOTALL):
        return text

    for attempt in range(retries):
        try:
            result = translator.translate(text, src='ja', dest='en').text
            result = normalize_quotes(result)
            return result
        except Exception as e:
            print(f"⚠️ 翻訳失敗（試行 {attempt+1}/{retries}）: {e}")
            time.sleep(2)
    return text

# === 差分チェック ===
def needs_translation(src_path, dest_path):
    """出力ファイルが存在しないか、元より古い場合のみ True"""
    if not os.path.exists(dest_path):
        return True
    src_mtime = os.path.getmtime(src_path)
    dest_mtime = os.path.getmtime(dest_path)
    return src_mtime > dest_mtime

# === メイン処理 ===
translated_count = 0
skipped_count = 0

for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    # 差分チェック
    if not needs_translation(src_path, dest_path):
        print(f"⏩ Skipped (no changes): {filename}")
        skipped_count += 1
        continue

    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # YAMLフロントマター分離
    if content.startswith("---"):
        try:
            _, fm, body = content.split('---', 2)
        except ValueError:
            print(f"⚠️ {filename} の front matter 分割に失敗。スキップします。")
            continue
    else:
        fm, body = "", content

    try:
        front_matter = yaml.safe_load(fm) or {}
    except yaml.YAMLError as e:
        print(f"⚠️ YAML構文エラー: {filename} ({e})")
        continue

    # タイトル翻訳
    title_ja = front_matter.get("title", "")
    if title_ja:
        title_en = translate_text(title_ja)
        front_matter["title_en"] = title_en

    # 言語指定
    front_matter["lang"] = "en"

    # 本文翻訳
    translated_body = ""
    for paragraph in body.split("\n\n"):
        translated_body += translate_text(paragraph) + "\n\n"

    output_content = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}"

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"✅ Translated: {filename}")
    translated_count += 1

print(f"\n🎉 English posts updated in '{DEST_DIR}'")
print(f"✅ 新規・更新翻訳: {translated_count} 件")
print(f"⏩ スキップ済み: {skipped_count} 件")
