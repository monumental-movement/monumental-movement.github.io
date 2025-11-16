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
    if is_non_translatable(text):
        return text
    try:
        result = translator.translate(str(text))
        if result is None:
            return str(text)
        if isinstance(result, str):
            return result
        return str(result)
    except Exception:
        return str(text)

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
    """
    日付や特殊文字を除き、URL向けに安全な slug を生成
    例: 2025-11-08-Stoned Baby and Join Clap – AK-47 EP.md
         → stoned-baby-and-join-clap-ak-47-ep
    """
    base = os.path.splitext(filename)[0]
    # 日付部分を削除
    base = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', base)
    # 半角スペースや特殊文字をハイフンに置換
    slug = re.sub(r'[^\w]+', '-', base)
    # 小文字化 & 前後ハイフン削除
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
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            translated_body += line + "\n"
            continue
        if in_code_block or is_non_translatable(line):
            translated_body += line + "\n"
        else:
            translated_body += translate_text(line) + "\n"

    # 出力
    output = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ Translated: {filename}")

print("\n🎉 Spanish translation completed successfully!")
