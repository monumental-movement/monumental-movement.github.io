import os
import yaml
import re
from deep_translator import GoogleTranslator
from difflib import unified_diff

SRC_DIR = "_posts"
DEST_DIR = os.path.join("es", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='es')


def is_non_translatable(line):
    """HTML・CSS・テーブル・コードを除外して誤検知を防ぐ"""
    stripped = line.strip()
    if not stripped:
        return True  # 空行
    # HTMLタグ (<div> 等)
    if re.fullmatch(r"<[^>]+>", stripped):
        return True
    # CSS ブロック (<style> または {...;} を含む行)
    if stripped.startswith("<style") or stripped.startswith("</style>"):
        return True
    if "{" in stripped and ";" in stripped and "}" in stripped:
        return True
    # Markdown table
    if stripped.startswith("|") and stripped.endswith("|"):
        return True
    # コードブロック開始・終了
    if stripped.startswith("```"):
        return True
    return False


def translate_text(text):
    """翻訳が必要な場合のみ DeepTranslator を実行"""
    if not isinstance(text, str):
        text = str(text)
    try:
        return translator.translate(text)
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
    except Exception:
        return {}


def extract_slug(filename):
    """日付や特殊文字を除き URL 用に安全な slug を生成"""
    base = os.path.splitext(filename)[0]
    base = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', base)
    slug = re.sub(r'[^\w]+', '-', base)
    slug = slug.lower().strip('-')
    return slug


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

    # Spanish 用 permalink を強制設定
    slug = extract_slug(filename)
    front_matter["lang"] = "es"
    front_matter["permalink"] = f"/es/{slug}/"

    # 本文翻訳
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

    # 翻訳除外判定
    if in_code_block or in_mermaid_block or is_non_translatable(line):
        translated_body += line + "\n"
    else:
        translated_body += translate_text(line) + "\n"

    # 出力
    output = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ Translated: {filename}")

print("\n🎉 Spanish translation completed successfully!")
