import os
import yaml
import re
from deep_translator import GoogleTranslator
from difflib import unified_diff
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
import hashlib

# ---------------------------------------------
# 設定
# ---------------------------------------------
SRC_DIR = "_posts"
DEST_DIR = os.path.join("zh-hant", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

# 並列処理のワーカー数（調整可能）
MAX_WORKERS = 5

# 翻訳キャッシュ（メモリ内）
translation_cache = {}

# Translator インスタンスはスレッドセーフではないため、各スレッドで生成
def get_translator():
    return GoogleTranslator(source='ja', target='zh-hant')


# =============================================
# キャッシュ機能付き翻訳
# =============================================
def translate_text_cached(text, translator):
    if not isinstance(text, str):
        text = str(text)
    
    # 空文字や短い文字列はそのまま返す
    if len(text.strip()) < 2:
        return text
    
    # キャッシュチェック
    cache_key = hashlib.md5(text.encode()).hexdigest()
    if cache_key in translation_cache:
        return translation_cache[cache_key]
    
    try:
        result = translator.translate(text)
        if result is None:
            result = text
        else:
            result = str(result)
        translation_cache[cache_key] = result
        return result
    except Exception:
        return text


# =============================================
# 翻訳除外ブロックの抽出（コンパイル済み正規表現）
# =============================================
EXCLUDE_BLOCK_PATTERNS = [
    (re.compile(r"<style[\s\S]*?</style>", re.MULTILINE), "STYLE"),
    (re.compile(r"<script[\s\S]*?</script>", re.MULTILINE), "SCRIPT"),
    (re.compile(r"<table[\s\S]*?</table>", re.MULTILINE), "TABLE"),
    (re.compile(r"<div class=\"mermaid\"[\s\S]*?</div>", re.MULTILINE), "MERMAID-WRAP"),
]


def extract_excluded_blocks(text):
    placeholders = {}
    idx = 0

    for pattern, tag in EXCLUDE_BLOCK_PATTERNS:
        matches = list(pattern.finditer(text))
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
# Mermaid 内ノード名・コメント翻訳（正規表現コンパイル済み）
# =============================================
MERMAID_COMMENT_PATTERN = re.compile(r"%%\s*(.*)")
MERMAID_NODE_PATTERNS = [
    re.compile(r'(\[)(.*?)(\])'),
    re.compile(r'(\()([^()]*)(\))'),
    re.compile(r'(\(\()([^()]*)(\)\))'),
    re.compile(r'(\|)(.*?)(\|)'),
]
JAPANESE_PATTERN = re.compile(r'[一-龯ぁ-んァ-ン]')


def translate_mermaid_line(line, translator):
    # コメント翻訳
    def repl_comment(m):
        return "%% " + translate_text_cached(m.group(1), translator)
    line = MERMAID_COMMENT_PATTERN.sub(repl_comment, line)

    # ノードラベル翻訳
    for pat in MERMAID_NODE_PATTERNS:
        def repl(m):
            start, text, end = m.group(1), m.group(2), m.group(3)
            if JAPANESE_PATTERN.search(text):
                translated = translate_text_cached(text, translator)
                return f"{start}{translated}{end}"
            return m.group(0)
        line = pat.sub(repl, line)

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
@lru_cache(maxsize=128)
def extract_slug(filename):
    base = os.path.splitext(filename)[0]
    base = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', base)
    slug = re.sub(r'[^\w]+', '-', base)
    return slug.lower().strip('-')


# =============================================
# 単一ファイル処理
# =============================================
def process_file(filename):
    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    # 翻訳除外ブロック退避
    cleaned_body, placeholders = extract_excluded_blocks(src_content)

    # front matter 抽出
    fm, body = split_front_matter(cleaned_body)
    front_matter = load_yaml_safe(fm)

    # 差分チェック
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            old = f.read()
        fm2, old_body = split_front_matter(old)
        diff = list(unified_diff(old_body.splitlines(), body.splitlines()))
        if not diff:
            return f"⏭️ No changes: {filename}"

    # Translator インスタンス取得
    translator = get_translator()

    # タイトル翻訳
    if front_matter.get("title"):
        front_matter["title"] = translate_text_cached(front_matter["title"], translator)
        slug = extract_slug(filename)
        front_matter["lang"] = "zh-hant"
        front_matter["permalink"] = f"/zh-hant/{slug}/"

    # 本文翻訳
    translated_body = ""
    in_code_block = False
    in_mermaid_block = False

    for line in body.splitlines():
        # コードブロック
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            translated_body += line + "\n"
            continue

        if in_code_block:
            translated_body += line + "\n"
            continue

        # Mermaid ブロック
        if line.strip().startswith("graph") or line.strip().startswith("flowchart"):
            in_mermaid_block = True
            translated_body += line + "\n"
            continue

        if in_mermaid_block:
            if line.strip() == "":
                translated_body += line + "\n"
                continue
            translated_body += translate_mermaid_line(line, translator) + "\n"
            continue

        if line.strip() == "</div>":
            in_mermaid_block = False
            translated_body += line + "\n"
            continue

        # 通常行翻訳
        translated_body += translate_text_cached(line, translator) + "\n"

    # 除外ブロック復元
    final_output = restore_excluded_blocks(
        f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}",
        placeholders
    )

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_output)

    return f"✅ Translated: {filename}"


# =============================================
# メイン処理（並列化）
# =============================================
if __name__ == "__main__":
    files = [f for f in os.listdir(SRC_DIR) if f.endswith(".md")]
    
    print(f"🚀 Processing {len(files)} files with {MAX_WORKERS} workers...\n")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(process_file, f): f for f in files}
        
        for future in as_completed(futures):
            result = future.result()
            print(result)

    print(f"\n🎉 zh-hant translation completed!")
    print(f"📊 Cache size: {len(translation_cache)} entries")