import os
import yaml
import re
from deep_translator import GoogleTranslator
from difflib import unified_diff

SRC_DIR = "_posts"
DEST_DIR = os.path.join("es", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='es')


# ------------------------------------------------
# 非翻訳判定
# ------------------------------------------------
def is_non_translatable(line):
    stripped = line.strip()
    if not stripped:
        return True
    if re.fullmatch(r"<[^>]+>", stripped):
        return True
    if stripped.startswith("<style") or stripped.startswith("</style>"):
        return True
    if "{" in stripped and ";" in stripped and "}" in stripped:
        return True
    if stripped.startswith("|") and stripped.endswith("|"):
        return True
    if stripped.startswith("```"):
        return True
    return False


# ------------------------------------------------
# 通常翻訳
# ------------------------------------------------
def translate_text(text):
    if not isinstance(text, str):
        text = str(text)
    try:
        return translator.translate(text)
    except Exception:
        return text


# ------------------------------------------------
# Mermaid 内のノード名・ラベルだけ翻訳
# ------------------------------------------------
def translate_mermaid_line(line):
    original = line

    # %% コメント翻訳
    def repl_comment(m):
        return "%% " + translate_text(m.group(1))

    line = re.sub(r"%%\s*(.*)", repl_comment, line)

    # ノードラベル構文をすべて翻訳対象にする
    patterns = [
        (r'(\[)(.*?)(\])'),
        (r'(\()([^()]*)(\))'),
        (r'(\(\()([^()]*)(\)\))'),
        (r'(\|)(.*?)(\|)'),
    ]

    for pat in patterns:
        def repl(m):
            start, text, end = m.group(1), m.group(2), m.group(3)
            # 日本語/漢字が含まれるときのみ翻訳
            if re.search(r'[一-龯ぁ-んァ-ン]', text):
                translated = translate_text(text)
                return f"{start}{translated}{end}"
            return m.group(0)

        line = re.sub(pat, repl, line)

    return line


# ------------------------------------------------
# YAML front matter
# ------------------------------------------------
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content


def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except Exception:
        return {}


# ------------------------------------------------
# URL slug 生成
# ------------------------------------------------
def extract_slug(filename):
    base = os.path.splitext(filename)[0]
    base = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', base)
    slug = re.sub(r'[^\w]+', '-', base)
    slug = slug.lower().strip('-')
    return slug


# ------------------------------------------------
# メイン処理
# ------------------------------------------------
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

    # Spanish permalink 生成
    slug = extract_slug(filename)
    front_matter["lang"] = "es"
    front_matter["permalink"] = f"/es/{slug}/"

    # ------------------------------------------------
    # 本文翻訳
    # ------------------------------------------------
    translated_body = ""
    in_code_block = False
    in_mermaid_block = False

    for line in body.splitlines():

        # Mermaid 開始
        if '<div class="mermaid">' in line:
            in_mermaid_block = True
            translated_body += line + "\n"
            continue

        # Mermaid 終了
        if '</div>' in line and in_mermaid_block:
            in_mermaid_block = False
            translated_body += line + "\n"
            continue

        # コードブロック
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            translated_body += line + "\n"
            continue

        # ------------------------------------------------
        # Mermaid ブロック → ノード名翻訳
        # ------------------------------------------------
        if in_mermaid_block:
            translated_body += translate_mermaid_line(line) + "\n"
            continue

        # コードブロック → 翻訳しない
        if in_code_block:
            translated_body += line + "\n"
            continue

        # 通常部 → 翻訳
        translated_body += translate_text(line) + "\n"

    # 出力
    output = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ Translated: {filename}")

print("\n🎉 Spanish translation with Mermaid node translation completed!")
