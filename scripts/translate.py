import os
import yaml
import re
from deep_translator import GoogleTranslator
from difflib import unified_diff

SRC_DIR = "_posts"
DEST_DIR = os.path.join("en", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='en')


def normalize_quotes(text):
    """全角・特殊引用符を半角 " に統一"""
    if not text:
        return text
    text = re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)
    text = re.sub(r'``(.*?)``', r'"\1"', text)
    text = re.sub(r"''(.*?)''", r'"\1"', text)
    text = re.sub(r"\b'(.*?)'\b", r'"\1"', text)
    return text


def translate_text(text):
    """iframe・コード・空行をスキップして安全翻訳"""
    if not text.strip():
        return text
    if re.search(r'<iframe.*?</iframe>', text, re.DOTALL):
        return text
    if re.match(r"^```", text.strip()):
        return text
    try:
        result = translator.translate(text)
        return normalize_quotes(result)
    except Exception as e:
        print(f"⚠️ 翻訳失敗: {e}")
        return text


def split_front_matter(content):
    """YAML front matter を分離して安全に返す"""
    if content.startswith("---"):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm, body = parts[1], parts[2]
            return fm, body
        else:
            # 不完全な場合でも空のfront matterを返す
            return "", content
    return "", content


def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except yaml.YAMLError:
        return {}


for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    fm, body = split_front_matter(src_content)
    front_matter = load_yaml_safe(fm)

    # 既存英語ファイルがある場合、差分を確認
    old_body = ""
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            dest_content = f.read()
        fm2, old_body = split_front_matter(dest_content)

    # 差分検出
    if old_body.strip():
        diff = list(unified_diff(old_body.splitlines(), body.splitlines()))
        if not diff:
            print(f"⏭️ No changes: {filename}")
            continue  # 変更なしならスキップ
        else:
            print(f"🔁 Diff detected: {filename} — 更新箇所を翻訳")

    # タイトル翻訳
    if front_matter.get("title"):
        front_matter["title"] = translate_text(front_matter["title"])

    front_matter["lang"] = "en"

    # 本文翻訳（コードブロックはスキップ）
    translated_body = ""
    in_code_block = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            translated_body += line + "\n"
            continue
        if in_code_block:
            translated_body += line + "\n"
        else:
            translated_body += translate_text(line) + "\n"

    # 英語ファイル出力
    output_content = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}"

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"✅ Translated/Updated: {filename}")

print("\n🎉 English posts updated successfully (only changed parts retranslated)")
