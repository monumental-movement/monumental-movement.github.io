import os
import yaml
import re
from deep_translator import GoogleTranslator
from difflib import unified_diff

SRC_DIR = "_posts"
DEST_DIR = os.path.join("en", "_posts")
CACHE_FILE = "translation_cache.yaml"

os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='en')

# --- キャッシュ読み込み ---
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        translation_cache = yaml.safe_load(f) or {}
else:
    translation_cache = {}

def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(translation_cache, f, allow_unicode=True)

def normalize_quotes(text):
    if not text:
        return text
    text = re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)
    return text

# --- 段落単位翻訳 ---
def translate_text_with_paragraphs(text):
    paragraphs = text.split("\n\n")  # 空行で段落分割
    translated_paragraphs = []

    for para in paragraphs:
        para = para.strip()
        if not para:
            translated_paragraphs.append("")
            continue
        if para in translation_cache:
            translated_paragraphs.append(translation_cache[para])
        else:
            try:
                result = translator.translate(para)
                if result is None:
                    result = para
                result = normalize_quotes(result)
                translation_cache[para] = result
                translated_paragraphs.append(result)
            except Exception as e:
                print(f"⚠️ 翻訳失敗: {e} — スキップ")
                translated_paragraphs.append(para)

    return "\n\n".join(translated_paragraphs)

# --- Front Matter 分割 ---
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
        else:
            return "", content
    return "", content

# --- 翻訳対象ブロック抽出 ---
def extract_translatable_blocks(body):
    blocks = []
    buf = []
    in_code = False

    for line in body.splitlines(True):  # 改行維持
        if line.strip().startswith("```"):
            if buf:
                blocks.append(("text", "".join(buf)))
                buf = []
            blocks.append(("code", line))
            in_code = not in_code
            continue

        if in_code or "<iframe" in line:
            blocks.append(("code", line))
        else:
            buf.append(line)

    if buf:
        blocks.append(("text", "".join(buf)))

    return blocks

# --- 組み戻し ---
def reconstruct_body(blocks, translated_texts):
    out = []
    t_idx = 0
    for btype, content in blocks:
        if btype == "code":
            out.append(content)
        else:
            out.append(translated_texts[t_idx])
            t_idx += 1
    return "".join(out)

# --- メイン処理 ---
for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    fm, body = split_front_matter(src_content)
    front_matter = yaml.safe_load(fm) or {}

    # --- 既存差分チェック ---
    old_body = ""
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            dest_content = f.read()
        _, old_body = split_front_matter(dest_content)

    if old_body.strip() == body.strip():
        print(f"⏭️ No changes: {filename}")
        continue

    print(f"🔁 Updating: {filename}")

    # --- タイトル翻訳 ---
    if front_matter.get("title"):
        front_matter["title"] = translate_text_with_paragraphs(front_matter["title"])

    front_matter["lang"] = "en"

    # --- 本文翻訳 ---
    blocks = extract_translatable_blocks(body)
    texts_to_translate = [b[1] for b in blocks if b[0] == "text"]
    translated_texts = [translate_text_with_paragraphs(t) for t in texts_to_translate]
    translated_body = reconstruct_body(blocks, translated_texts)

    # --- ファイル書き出し ---
    output = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ Done: {filename}\n")

# --- キャッシュ保存 ---
save_cache()
print("🎉 Finished (paragraph-level translation with cache)")
