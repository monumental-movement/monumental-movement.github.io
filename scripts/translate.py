import os
import re
import yaml
from deep_translator import GoogleTranslator

SRC_DIR = "_posts"
DEST_DIR = "en/_posts"

translator = GoogleTranslator(source="ja", target="en")
os.makedirs(DEST_DIR, exist_ok=True)

print("🌐 Starting translation with YAML safety check...")

def sanitize_text(text):
    """Jekyll/YAMLを壊さないように危険文字を整形"""
    text = text.replace("\r", "")
    # YAML境界を回避
    text = re.sub(r"^-{3,}$", "--- ", text, flags=re.MULTILINE)
    # コロン後にスペースを確保
    text = re.sub(r":(?!\s)", ": ", text)
    # クォートの暴走防止
    text = text.replace('"', "'")
    return text

for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # --- YAMLフロントマター分離 ---
    if content.startswith("---"):
        parts = re.split(r"^---\s*$", content, flags=re.MULTILINE)
        if len(parts) >= 3:
            front_matter = parts[1].strip()
            body = parts[2].strip()
        else:
            front_matter = ""
            body = content
    else:
        front_matter = ""
        body = content

    # --- YAMLを安全に読み込めるか確認 ---
    try:
        yaml.safe_load(front_matter)
    except yaml.YAMLError as e:
        print(f"⚠️ YAML broken in {filename}: {e}")
        continue

    # --- 英訳ファイルが存在すればスキップ ---
    if os.path.exists(dest_path):
        print(f"⏩ Skipping (exists): {filename}")
        continue

    print(f"🌍 Translating: {filename}")

    try:
        translated_body = translator.translate(body)
    except Exception as e:
        print(f"⚠️ Translation failed for {filename}: {e}")
        continue

    # --- テキスト整形 ---
    translated_body = sanitize_text(translated_body)

    translated_content = f"---\n{front_matter}\nlang: en\n---\n\n{translated_body}\n"

    # --- YAMLとして最終検証 ---
    try:
        _ = yaml.safe_load(re.split(r"^---\s*$", translated_content, flags=re.MULTILINE)[1])
    except Exception as e:
        print(f"❌ YAML validation failed for {filename}: {e}")
        continue

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(translated_content)

    print(f"✅ Saved: {dest_path}")

print("\n🎉 All translations completed safely (validated YAML)")
