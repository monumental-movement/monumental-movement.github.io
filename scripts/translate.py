import os
import yaml
import re
from deep_translator import GoogleTranslator
from difflib import unified_diff

SRC_DIR = "_posts"
DEST_DIR = os.path.join("en", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='en')


def normalize_quotes(text):
    if not text:
        return text
    text = re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)
    return text


def translate_block(text):
    """本文を丸ごと翻訳（コード・iframeは事前除外）"""
    if not text.strip():
        return text
    try:
        res = translator.translate(text)
        if res is None:
            return text
        return normalize_quotes(res)
    except:
        return text


def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
        else:
            return "", content
    return "", content


def extract_translatable_blocks(body):
    """コードブロック・iframe を保持しつつ、翻訳ブロックだけ抽出"""
    blocks = []
    buf = []
    in_code = False

    for line in body.splitlines(True):  # keep \n
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


def reconstruct_body(blocks, translated_texts):
    """ブロックを組み戻す"""
    out = []
    t_idx = 0
    for btype, content in blocks:
        if btype == "code":
            out.append(content)
        else:
            out.append(translated_texts[t_idx])
            t_idx += 1
    return "".join(out)


for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    fm, body = split_front_matter(src_content)
    front_matter = yaml.safe_load(fm) or {}

    # 既存差分チェック
    old_body = ""
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            dest_content = f.read()
        _, old_body = split_front_matter(dest_content)

    if old_body.strip() == body.strip():
        print(f"⏭️ No changes: {filename}")
        continue

    print(f"🔁 Updating: {filename}")

    # タイトル翻訳
    if front_matter.get("title"):
        front_matter["title"] = translate_block(front_matter["title"])

    front_matter["lang"] = "en"

    # 本文ブロック抽出
    blocks = extract_translatable_blocks(body)

    # 翻訳（ここが爆速ポイント：行でなく「まとまりごと」）
    texts_to_translate = [b[1] for b in blocks if b[0] == "text"]
    translated_texts = [translate_block(t) for t in texts_to_translate]

    # 組み戻し
    translated_body = reconstruct_body(blocks, translated_texts)

    # 書き出し
    output = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ Done: {filename}\n")

print("🎉 Finished (block-level fast translation)")
