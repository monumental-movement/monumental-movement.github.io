# scripts/translate.py
# 日本語Markdownを英語に自動翻訳して /en/_posts に出力する最小構成版
from googletrans import Translator
import os

SRC_DIR = "_posts"
DEST_DIR = "en/_posts"

translator = Translator()

os.makedirs(DEST_DIR, exist_ok=True)

for filename in os.listdir(SRC_DIR):
    if filename.endswith(".md"):
        src_path = os.path.join(SRC_DIR, filename)
        dest_path = os.path.join(DEST_DIR, filename)

        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()

        print(f"Translating {filename} ...")
        translated_text = translator.translate(content, src='ja', dest='en').text

        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(translated_text)

print("✅ Translation complete! English files are in /en/_posts/")
