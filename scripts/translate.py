# scripts/translate.py
import os
from deep_translator import GoogleTranslator

SRC_DIR = "_posts"
DEST_DIR = "en/_posts"

translator = GoogleTranslator(source="ja", target="en")

os.makedirs(DEST_DIR, exist_ok=True)

for filename in os.listdir(SRC_DIR):
    if filename.endswith(".md"):
        src_path = os.path.join(SRC_DIR, filename)
        dest_path = os.path.join(DEST_DIR, filename)
        print(f"🌍 Translating {filename} ...")
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()
        try:
            translated_text = translator.translate(content)
        except Exception as e:
            print(f"⚠️ Translation failed for {filename}: {e}")
            continue
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(translated_text)
print("✅ Translation complete! English files are in /en/_posts/")
