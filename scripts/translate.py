import os
from deep_translator import GoogleTranslator

# --- 設定 ---
SRC_DIR = "_posts"         # 日本語記事の場所
DEST_DIR = "en/_posts"     # 英訳を出力する場所

# --- 翻訳エンジン設定 ---
translator = GoogleTranslator(source="ja", target="en")

# --- 出力フォルダを作成 ---
os.makedirs(DEST_DIR, exist_ok=True)

print("🌐 Starting translation process...")

# --- 記事を1つずつ処理 ---
for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    if not os.path.exists(src_path):
        print(f"⚠️ Source not found: {src_path}")
        continue

    # ✅ 英語版がすでに存在する場合はスキップ（安全運用モード）
    if os.path.exists(dest_path):
        print(f"⏩ Skipping (already exists): {filename}")
        continue

    print(f"🌍 Translating: {filename}")
    try:
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 翻訳を実行
        translated_text = translator.translate(content)

        # ✅ 日本語記事は上書きしない。英語フォルダにのみ書き込む。
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(translated_text)

        print(f"✅ Saved: {dest_path}")

    except Exception as e:
        print(f"⚠️ Translation failed for {filename}: {e}")
        continue

print("\n🎉 All translations complete!")
print("日本語記事 (_posts/) は安全に保持され、英訳は en/_posts/ に保存されました。")
