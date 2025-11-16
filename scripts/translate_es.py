import os
import yaml
import re
from deep_translator import GoogleTranslator
from difflib import unified_diff

# ---------------------------------------------
# 設定
# ---------------------------------------------
SRC_DIR = "_posts"
DEST_DIR = os.path.join("es", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='es')


# =============================================
# 1) 翻訳除外ブロックの抽出
# =============================================
EXCLUDE_BLOCK_PATTERNS = [
    (r"<style[\s\S]*?</style>", "STYLE"),
    (r"<script[\s\S]*?</script>", "SCRIPT"),
    (r"<table[\s\S]*?</table>", "TABLE"),
    (r"<div class=\"mermaid\"[\s\S]*?</div>", "MERMAID-WRAP"),
]


def extract_excluded_blocks(text):
    placeholders = {}
    idx = 0

    for pattern, tag in EXCLUDE_BLOCK_PATTERNS:
        matches = list(re.finditer(pattern, text, re.MULTILINE))
        for m in matches:
            block = m.group(0)
            placeholder = f"__EXCLUDE_{tag}_{idx}__"
            placeholders[placeholder] = block
            text = text.replace(block, placeholder)
            idx += 1

    return text, placeholders


def restore_excluded_blocks(text, placeholders):
    for ph, block in placeholders.items():
        text = text.replace(ph, block)
    return text


# =============================================
# 翻訳（Deep Translator）
# =============================================
def translate_text(text):
    if not isinstance(text, str):
        text = str(text)
    try:
        result = translator.translate(text)
        if result is None:
            return text
        return str(result)
    except Exception:
        return text


# =============================================
# Mermaid 内ノード名・コメント翻訳
# =============================================
def translate_mermaid_line(line):
    # %% コメント翻訳
    def repl_comment(m):
        return "%% " + translate_text(m.group(1))
    line = re.sub(r"%%\s*(.*)", repl_comment, line)

    # ノードラベル構文翻訳
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
            return m.group(0)

        line = re.sub(pat, repl, line)

    return line


# =============================================
# YAML front matter
# =============================================
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


# =============================================
# URL slug 生成
# =============================================
def extract_slug(filename):
    base = os.path.splitext(filename)[0]
    base = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', base)
    slug = re.sub(r'[^\w]+', '-', base)
    return slug.lower().strip('-')


# =============================================
# メイン処理
# =============================================
for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    # ---------------------------------------
    # ① まず翻訳除外ブロックを丸ごと退避
    # ---------------------------------------
    cleaned_body, placeholders = extract_excluded_blocks(src_content)

    # front matter 抽出し直し（退避後のtext）
    fm, body = split_front_matter(cleaned_body)
    front_matter = load_yaml_safe(fm)

    # 既存ファイル差分チェック
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

    # permalink
    slug = extract_slug(filename)
    front_matter["lang"] = "es"
    front_matter["permalink"] = f"/es/{slug}/"

    # ---------------------------------------
    # ② cleaned body の本文行ごと翻訳
    # ---------------------------------------
    translated_body = ""

    in_code_block = False
    in_mermaid_block = False

    for line in body.splitlines():
        # コード（```）
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            translated_body += line + "\n"
            continue

        if in_code_block:
            translated_body += line + "\n"
            continue

        # Mermaid ブロック本体
        if line.strip().startswith("graph") or line.strip().startswith("flowchart"):
            in_mermaid_block = True
            translated_body += line + "\n"
            continue

        if in_mermaid_block:
            # Mermaid ノード翻訳
            if line.strip() == "":
                translated_body += line + "\n"
                continue
            translated_body += translate_mermaid_line(line) + "\n"
            continue

        # Mermaid 終了判定
        if line.strip() == "</div>":
            in_mermaid_block = False
            translated_body += line + "\n"
            continue

        # 通常行翻訳
        translated_body += translate_text(line) + "\n"

    # ---------------------------------------
    # ③ 除外した block を元に戻す
    # ---------------------------------------
    final_output = restore_excluded_blocks(
        f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}",
        placeholders
    )

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_output)

    print(f"✅ Translated: {filename}")

print("\n🎉 Spanish translation with SAFE exclusion and Mermaid node translation completed!")
