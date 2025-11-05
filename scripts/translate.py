import os
import yaml
import re
from deep_translator import GoogleTranslator

# 翻訳元・翻訳先ディレクトリ
SRC_DIR = "_posts"
DEST_DIR = os.path.join("en", "_posts")

# 出力ディレクトリが無ければ作成
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='en')


def normalize_quotes(text):
    """全角・特殊引用符をすべて半角の " に統一"""
    text = "" if text is None else str(text)
    text = re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)
    text = re.sub(r'``(.*?)``', r'"\1"', text)
    text = re.sub(r"''(.*?)''", r'"\1"', text)
    text = re.sub(r"\b'(.*?)'\b", r'"\1"', text)
    return text


def translate_text(text):
    """空行・iframe・短文・コードブロックを考慮して安全に翻訳（常に str を返す）"""
    if text is None:
        return ""
    if not isinstance(text, str):
        text = str(text)
    if not text.strip():
        return text

    # iframeタグ・コードブロックをスキップ
    if re.search(r'<iframe.*?</iframe>', text, re.DOTALL):
        return text
    if re.match(r"^```", text.strip()):
        return text

    try:
        result = translator.translate(text)
        if not result:
            return text
        result = normalize_quotes(result)
        return str(result) if result is not None else text
    except Exception as e:
        print(f"⚠️ 翻訳失敗: {e}")
        return text


# --- 全記事を強制翻訳 ---
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

    # タイトル翻訳（日本語タイトル削除 → 英語タイトルに上書き）
    title_ja = front_matter.get("title", "")
    if title_ja:
        title_en = translate_text(title_ja)
        front_matter["title"] = title_en

    # 言語指定
    front_matter["lang"] = "en"

    # 本文を翻訳（コードブロックをスキップ）
    translated_body = ""
    in_code_block = False

    for line in body.splitlines():
        # コードブロックの開始・終了判定
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            translated_body += line + "\n"
            continue

        if in_code_block:
            translated_body += line + "\n"
        else:
            line_translated = translate_text(line)
            if line_translated is None:
                line_translated = line
            translated_body += str(line_translated) + "\n"

    # 出力ファイル構築
    output_content = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}"

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"✅ Translated (title replaced): {filename} → {dest_path}")

print("\n🎉 English posts generated successfully (titles in English only, all retranslated, no NoneType errors)")
