import os
import yaml
from googletrans import Translator

# 翻訳元・翻訳先ディレクトリ
SRC_DIR = "_posts"
DEST_DIR = os.path.join("en", "_posts")

# 出力ディレクトリが無ければ作成
os.makedirs(DEST_DIR, exist_ok=True)

translator = Translator()

def translate_text(text):
    """空行や短文を考慮して安全に翻訳"""
    if not text.strip():
        return text
    try:
        result = translator.translate(text, src='ja', dest='en').text
        return result
    except Exception as e:
        print(f"⚠️ 翻訳失敗: {e}")
        return text  # 失敗時は元の日本語を残す

for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # YAMLフロントマターを分離
    if content.startswith("---"):
        try:
            _, fm, body = content.split('---', 2)
        except ValueError:
            print(f"⚠️ {filename} の front matter 分割に失敗しました。スキップします。")
            continue
    else:
        fm, body = "", content

    try:
        front_matter = yaml.safe_load(fm) or {}
    except yaml.YAMLError as e:
        print(f"⚠️ YAML構文エラー: {filename} ({e})")
        continue

    # タイトル翻訳（英語タイトルを追加）
    title_ja = front_matter.get("title", "")
    if title_ja:
        title_en = translate_text(title_ja)
        front_matter["title_en"] = title_en

    # 言語指定
    front_matter["lang"] = "en"

    # 本文を翻訳
    translated_body = ""
    for paragraph in body.split("\n\n"):
        translated_body += translate_text(paragraph) + "\n\n"

    # 出力ファイル構築
    output_content = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}"

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"✅ Translated: {filename} → {dest_path}")

print("\n🎉 Translation completed successfully! English posts saved in 'en/_posts/'")
