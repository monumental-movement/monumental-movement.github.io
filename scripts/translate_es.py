import os
import yaml
import re
from googletrans import Translator
from difflib import unified_diff

SRC_DIR = "_posts"
DEST_DIR = os.path.join("es", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='es')

def is_non_translatable(line):
    """CSS, HTML, table, code, style を検知して完全スキップ"""
    if not line.strip():
        return True

    # HTMLタグ
    if re.match(r"\s*<[^>]+>\s*$", line):
        return True

    # CSS ブロック
    if re.match(r".*\{.*\}", line):
        return True

    # <style> ブロック
    if "<style" in line.lower() or "</style>" in line.lower():
        return True

    # テーブル (Markdown)
    if re.match(r"^\|.*\|$", line.strip()):
        return True

    # コードブロック
    if line.strip().startswith("```"):
        return True

    return False


def translate_text(text):
    if is_non_translatable(text):
        return text

    try:
        result = translator.translate(text, src="ja", dest="es")
        return result.text
    except Exception:
        return text


def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content


def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except:
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

    # 差分チェック
    old_body = ""
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            old = f.read()
        fm2, old_body = split_front_matter(old)

        diff = list(unified_diff(old_body.splitlines(), body.splitlines()))
        if not diff:
            print(f"⏭️ No changes: {filename}")
            continue
        else:
            print(f"🔁 Diff detected: {filename}")

    # タイトル翻訳
    if front_matter.get("title"):
        front_matter["title"] = translate_text(front_matter["title"])

    front_matter["lang"] = "es"

    # 本文翻訳
    translated_body = ""
    in_code_block = False

    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            translated_body += line + "\n"
            continue

        if in_code_block or is_non_translatable(line):
            translated_body += line + "\n"
        else:
            translated_body += translate_text(line) + "\n"

    output = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}"

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ Translated: {filename}")

print("\n🎉 Spanish translation completed safely (HTML/CSS protected)")
