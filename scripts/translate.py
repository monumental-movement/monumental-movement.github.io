import os
import yaml
import re
from deep_translator import GoogleTranslator
from difflib import unified_diff

SRC_DIR = "_posts"
DEST_DIR = os.path.join("en", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='en')


# -----------------------------
# 基本：安全翻訳
# -----------------------------
def normalize_quotes(text):
    if not text:
        return text
    text = re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)
    text = re.sub(r'``(.*?)``', r'"\1"', text)
    text = re.sub(r"''(.*?)''", r'"\1"', text)
    text = re.sub(r"\b'(.*?)'\b", r'"\1"', text)
    return text


def translate_text(text):
    """Mermaid以外の通常文章の翻訳"""
    if not text.strip():
        return text
    if re.search(r'<iframe.*?</iframe>', text, re.DOTALL):
        return text
    if re.match(r"^```", text.strip()):
        return text
    try:
        result = translator.translate(text)
        if result is None:
            print(f"⚠️ None returned: {text[:30]}...")
            return text
        return normalize_quotes(str(result))
    except Exception as e:
        print(f"⚠️ 翻訳失敗: {e}")
        return text


# -----------------------------
# Mermaid ブロックの専用翻訳
# -----------------------------
def translate_mermaid_line(line):
    original = line

    # %% コメント
    def repl_comment(m):
        text = m.group(1)
        return "%% " + translate_text(text)

    line = re.sub(r"%%\s*(.*)", repl_comment, line)

    # [label] / (label) / ((label)) / |label|
    patterns = [
        (r'(\[)(.*?)(\])'),
        (r'(\()([^()]*)(\))'),
        (r'(\(\()([^()]*)(\)\))'),
        (r'(\|)(.*?)(\|)'),
    ]

    for pat in patterns:
        def repl(m):
            start, text, end = m.group(1), m.group(2), m.group(3)
            if re.search(r'[一-龯ぁ-んァ-ン]', text):
                translated = translate_text(text)
                return f"{start}{translated}{end}"
            else:
                return m.group(0)

        line = re.sub(pat, repl, line)

    return line


# -----------------------------
# YAML front matter
# -----------------------------
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
        else:
            return "", content
    return "", content


def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except yaml.YAMLError:
        return {}


# -----------------------------
# メイン処理
# -----------------------------
for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    fm, body = split_front_matter(src_content)
    front_matter = load_yaml_safe(fm)

    # 既存ファイル → 差分チェック
    old_body = ""
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            dest_content = f.read()
        fm2, old_body = split_front_matter(dest_content)

    if old_body.strip():
        diff = list(unified_diff(old_body.splitlines(), body.splitlines()))
        if not diff:
            print(f"⏭️ No changes: {filename}")
            continue
        else:
            print(f"🔁 Diff detected: {filename}")

    # タイトル翻訳
    if front_matter.get("title"):
        front_matter["title"] = translate_text(front_matter["title"])
    front_matter["lang"] = "en"

    # 本文翻訳開始
    translated_body = ""
    in_code_block = False
    in_mermaid_block = False

    for line in body.splitlines():
        # Mermaid開始
        if '<div class="mermaid">' in line:
            in_mermaid_block = True
            translated_body += line + "\n"
            continue

        # Mermaid終了
        if '</div>' in line and in_mermaid_block:
            in_mermaid_block = False
            translated_body += line + "\n"
            continue

        # コードブロック開始/終了
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            translated_body += line + "\n"
            continue

        # 翻訳分岐
        if in_mermaid_block:
            translated_body += translate_mermaid_line(line) + "\n"
        elif in_code_block:
            translated_body += line + "\n"
        else:
            translated_body += translate_text(line) + "\n"

    # 出力
    output_content = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}"

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"✅ Translated/Updated: {filename}")

print("\n🎉 English posts updated successfully!")
