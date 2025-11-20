import os
import yaml
import re
from deep_translator import GoogleTranslator

# ---------------------------------------------
# CONFIG
# ---------------------------------------------
SRC_DIR = "_posts"
DEST_DIR = os.path.join("ko", "_posts")  # Korean posts
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='ko')


# =============================================
# 1) EXCLUDE BLOCK PATTERNS
# =============================================
EXCLUDE_BLOCK_PATTERNS = [
    (r"<style[\s\S]*?</style>", "STYLE"),
    (r"<script[\s\S]*?</script>", "SCRIPT"),
    (r"<table[\s\S]*?</table>", "TABLE"),
    (r"<div class=\"mermaid\"[\s\S]*?</div>", "MERMAID"),
    (r"```[\s\S]*?```", "CODEBLOCK"),
]


def extract_excluded_blocks(text):
    placeholders = {}
    idx = 0

    for pattern, tag in EXCLUDE_BLOCK_PATTERNS:
        for m in re.finditer(pattern, text):
            block = m.group(0)
            ph = f"__EXCLUDE_{tag}_{idx}__"
            placeholders[ph] = block
            text = text.replace(block, ph)
            idx += 1

    return text, placeholders


def restore_excluded_blocks(text, placeholders):
    for ph, block in placeholders.items():
        text = text.replace(ph, block)
    return text


# =============================================
# 2) TRANSLATION WRAPPER
# =============================================
def translate_text_fast(text):
    """Wrap GoogleTranslator to avoid crashes."""
    try:
        t = translator.translate(text)
        return t if t else text
    except Exception:
        return text


# =============================================
# 3) YAML HANDLING
# =============================================
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content


def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except:
        return {}


def extract_slug(filename):
    base = os.path.splitext(filename)[0]
    base = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', base)
    slug = re.sub(r'[^\w]+', '-', base)
    return slug.lower().strip('-')


# =============================================
# 4) MAIN
# =============================================
for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    print("🔄 Processing:", filename)

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # -----------------------------------------
    # A) EXCLUDE ALL BLOCKS
    # -----------------------------------------
    tmp, placeholders = extract_excluded_blocks(content)

    # -----------------------------------------
    # B) SPLIT FRONT MATTER
    # -----------------------------------------
    fm, body = split_front_matter(tmp)
    fm_dict = load_yaml_safe(fm)

    # translate title
    if fm_dict.get("title"):
        fm_dict["title"] = translate_text_fast(fm_dict["title"])

    slug = extract_slug(filename)
    fm_dict["lang"] = "ko"
    fm_dict["permalink"] = f"/ko/{slug}/"

    # -----------------------------------------
    # C) BODY — TRANSLATE ALL AT ONCE
    # -----------------------------------------
    translated_body = translate_text_fast(body)

    # -----------------------------------------
    # D) RESTORE BLOCKS
    # -----------------------------------------
    final = f"---\n{yaml.safe_dump(fm_dict, allow_unicode=True)}---\n{translated_body}"
    final = restore_excluded_blocks(final, placeholders)

    # -----------------------------------------
    # E) SAVE
    # -----------------------------------------
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final)

    print("✅ Done:", filename)

print("\n🎉 Korean FAST translation completed!")
