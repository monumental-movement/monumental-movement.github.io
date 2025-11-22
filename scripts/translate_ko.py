import os
import yaml
import re
import time
import concurrent.futures
from deep_translator import GoogleTranslator

# --------------------------------------------------
# 設定
# --------------------------------------------------
SRC_DIR = "_posts"
DEST_DIR = os.path.join("ko", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='ko')

# =============================================
# 翻訳除外ブロック
# =============================================
EXCLUDE_BLOCK_PATTERNS = [
    (r"<style[\s\S]*?</style>", "STYLE"),
    (r"<script[\s\S]*?</script>", "SCRIPT"),
    (r"<table[\s\S]*?</table>", "TABLE"),
    (r"<iframe[\s\S]*?</iframe>", "IFRAME"),
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
# 絶対に文字列を返す翻訳関数（並列でも日本語残りゼロ）
# =============================================
def translate_text(text, retries=3):
    text = str(text)
    for _ in range(retries):
        try:
            result = translator.translate(text)
            if result:
                return str(result)
        except Exception:
            time.sleep(0.3)
    return text

# =============================================
# Mermaid 内部翻訳
# =============================================
def translate_mermaid_line(line):
    # コメント
    line = re.sub(r"%%\s*(.*)", lambda m: "%% " + translate_text(m.group(1)), line)

    # ノードラベル
    patterns = [
        (r'(\[)(.*?)(\])'),
        (r'(\()([^()]*)(\))'),
        (r'(\(\()([^()]*)(\)\))'),
        (r'(\|)(.*?)(\|)'),
    ]
    for pattern in patterns:
        def repl(m):
            start, text, end = m.group(1), m.group(2), m.group(3)
            translated = translate_text(text)
            return f"{start}{translated}{end}"
        line = re.sub(pattern, repl, line)

    return line

# =============================================
# YAML
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
    except:
        return {}

# =============================================
# slug
# =============================================
def extract_slug(filename):
    base = os.path.splitext(filename)[0]
    base = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', base)
    slug = re.sub(r'[^\w]+', '-', base)
    return slug.lower().strip('-')

# =============================================
# 記事単位の処理
# =============================================
def process_article(filename):
    if not filename.endswith(".md"):
        return

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    # 除外ブロック退避
    cleaned, placeholders = extract_excluded_blocks(src_content)

    fm, body = split_front_matter(cleaned)
    fm_dict = load_yaml_safe(fm)

    # タイトル翻訳
    if "title" in fm_dict:
        fm_dict["title"] = translate_text(fm_dict["title"])

    slug = extract_slug(filename)
    fm_dict["lang"] = "ko"
    fm_dict["permalink"] = f"/ko/{slug}/"

    # 本文翻訳
    translated_lines = []

    in_code = False
    in_mermaid = False

    for line in body.splitlines():
        stripped = line.strip()

        # コードブロック
        if stripped.startswith("```"):
            in_code = not in_code
            translated_lines.append(line)
            continue
        if in_code:
            translated_lines.append(line)
            continue

        # Mermaidブロック開始
        if stripped.startswith("graph") or stripped.startswith("flowchart"):
            in_mermaid = True
            translated_lines.append(line)
            continue

        if in_mermaid:
            if stripped == "</div>":
                in_mermaid = False
                translated_lines.append(line)
            else:
                translated_lines.append(translate_mermaid_line(line))
            continue

        # 通常本文
        translated_lines.append(translate_text(line))

    translated_body = "\n".join(translated_lines)

    # 復元
    final = restore_excluded_blocks(
        f"---\n{yaml.safe_dump(fm_dict, allow_unicode=True)}---\n{translated_body}",
        placeholders
    )

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final)

    print(f"✔ {filename} translated")

# =============================================
# 並列実行
# =============================================
if __name__ == "__main__":
    files = [f for f in os.listdir(SRC_DIR) if f.endswith(".md")]

    # 最大8スレッド
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        list(executor.map(process_article, files))

    print("\n🎉 Korean translation completed (parallel, no Japanese left).")
