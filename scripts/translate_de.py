import os
import yaml
import re
from deep_translator import GoogleTranslator
from difflib import unified_diff

# ---------------------------------------------------------
# 設定
# ---------------------------------------------------------
SRC_DIR = "_posts"
DEST_DIR = os.path.join("de", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source="ja", target="de")

# 翻訳キャッシュ
TRANSLATION_CACHE = {}
CACHE_FILE = "translation_cache_de.json"


# ---------------------------------------------------------
# キャッシュ読み込み / 保存
# ---------------------------------------------------------
import json

if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        TRANSLATION_CACHE = json.load(f)


def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(TRANSLATION_CACHE, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------
# 翻訳（キャッシュ付き）
# ---------------------------------------------------------
def translate_text(text):
    if not isinstance(text, str):
        text = str(text)

    if text in TRANSLATION_CACHE:
        return TRANSLATION_CACHE[text]

    try:
        translated = translator.translate(text)
        if translated is None:
            translated = text

        TRANSLATION_CACHE[text] = translated
        return translated

    except Exception:
        return text


# ---------------------------------------------------------
# 翻訳除外ブロック（Mermaid / table / style / script）
# ---------------------------------------------------------
EXCLUDE_BLOCK_PATTERNS = [
    (r"<style[\s\S]*?</style>", "STYLE"),
    (r"<script[\s\S]*?</script>", "SCRIPT"),
    (r"<table[\s\S]*?</table>", "TABLE"),
    (r"<div class=\"mermaid\"[\s\S]*?</div>", "MERMAID"),
]


def extract_excluded_blocks(text):
    placeholders = {}
    idx = 0

    for pattern, tag in EXCLUDE_BLOCK_PATTERNS:
        for m in list(re.finditer(pattern, text, re.MULTILINE)):
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


# ---------------------------------------------------------
# 段落単位翻訳（高速化の核心）
# ---------------------------------------------------------
def translate_paragraphs(text):
    paragraphs = text.split("\n\n")
    result = []
    for p in paragraphs:
        if re.search(r"[一-龯ぁ-んァ-ン]", p):
            result.append(translate_text(p))
        else:
            result.append(p)
    return "\n\n".join(result)


# ---------------------------------------------------------
# Mermaid コメント翻訳のみ
# ---------------------------------------------------------
def translate_mermaid_block(block):
    lines = block.splitlines()
    result = []

    for line in lines:
        # コメント行だけ翻訳する
        if line.strip().startswith("%%"):
            m = re.match(r"%%\s*(.*)", line)
            if m:
                translated = translate_text(m.group(1))
                result.append("%% " + translated)
            else:
                result.append(line)
        else:
            result.append(line)

    return "\n".join(result)


# ---------------------------------------------------------
# YAML front matter
# ---------------------------------------------------------
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content


def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except Exception:
        return {}


# ---------------------------------------------------------
# slug
# ---------------------------------------------------------
def extract_slug(filename):
    base = os.path.splitext(filename)[0]
    base = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", base)
    slug = re.sub(r"[^\w]+", "-", base)
    return slug.lower().strip("-")


# ---------------------------------------------------------
# 本文の除外ブロック以外を再び Mermaid も分割
# ---------------------------------------------------------
def process_body(body):
    segments = re.split(r"(<div class=\"mermaid\"[\s\S]*?</div>)", body)

    processed = []
    for seg in segments:
        if seg.startswith('<div class="mermaid"'):
            processed.append(seg)  # 全体は除外済みなのでそのまま
        else:
            processed.append(translate_paragraphs(seg))

    return "".join(processed)


# =========================================================
# メイン処理（高速・再開対応）
# =========================================================
for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    print(f"\n📄 Processing: {filename}")

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    # ① 翻訳除外ブロック退避
    cleaned_body, placeholders = extract_excluded_blocks(src_content)

    fm, body = split_front_matter(cleaned_body)
    front_matter = load_yaml_safe(fm)

    # 既存翻訳との差分によるスキップ
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            old = f.read()
        fm2, old_body = split_front_matter(old)

        diff = list(unified_diff(old_body.splitlines(), body.splitlines()))
        if not diff:
            print(f"⏭️ No changes → Skip: {filename}")
            continue
        else:
            print(f"🔁 Diff detected → Re-translate: {filename}")

    # ② front matter 翻訳
    if front_matter.get("title"):
        front_matter["title"] = translate_text(front_matter["title"])

    slug = extract_slug(filename)
    front_matter["lang"] = "de"
    front_matter["permalink"] = f"/de/{slug}/"

    # ③ 本文高速翻訳（段落ベース）
    new_body = process_body(body)

    # ④ 除外ブロック復元
    final_output = restore_excluded_blocks(
        f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{new_body}",
        placeholders
    )

    # 書き込み
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_output)

    print(f"🇩🇪✅ Translated: {filename}")

    # キャッシュ保存
    save_cache()

print("\n🎉 High-speed German translation completed with resume capability!")
