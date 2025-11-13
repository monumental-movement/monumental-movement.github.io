import os
import yaml
import re
from googletrans import Translator
from concurrent.futures import ThreadPoolExecutor

SRC_DIR = "_posts"
DEST_DIR = os.path.join("es", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

translator = Translator()
MAX_WORKERS = 4  # 並列数（環境に応じて調整）


def normalize_quotes(text):
    if not text:
        return text
    text = re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)
    text = re.sub(r'``(.*?)``', r'"\1"', text)
    text = re.sub(r"''(.*?)''", r'"\1"', text)
    text = re.sub(r"\b'(.*?)'\b", r'"\1"', text)
    return text


def translate_text(text):
    if not text.strip():
        return text
    if re.search(r'<iframe.*?</iframe>', text, re.DOTALL):
        return text
    if re.match(r"^```", text.strip()):
        return text
    try:
        result = translator.translate(text, src='ja', dest='es')
        if not result or not result.text:
            print(f"⚠️ 翻訳結果なし: {text[:30]}...")
            return text
        return normalize_quotes(result.text)
    except Exception as e:
        print(f"⚠️ 翻訳失敗: {e}（スキップ）")
        return text


def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm, body = parts[1], parts[2]
            return fm, body
        else:
            return "", content
    return "", content


def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except yaml.YAMLError:
        return {}


def normalize_body(text):
    return "\n".join(line.rstrip() for line in text.splitlines()).strip()


def process_file(filename):
    if not filename.endswith(".md"):
        return

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    fm, body = split_front_matter(src_content)
    front_matter = load_yaml_safe(fm)

    old_body = ""
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            dest_content = f.read()
        fm2, old_body = split_front_matter(dest_content)

    if normalize_body(old_body) == normalize_body(body):
        print(f"⏭️ No changes: {filename}")
        return

    print(f"🔁 Diff detected: {filename} — 更新箇所を翻訳")

    if front_matter.get("title"):
        front_matter["title"] = translate_text(front_matter["title"])
    front_matter["lang"] = "es"

    translated_body = []
    in_code_block = False
    buffer = []

    def flush_buffer():
        if buffer:
            text_to_translate = "\n".join(buffer)
            translated_body.extend(translate_text(text_to_translate).splitlines())
            buffer.clear()

    for line in body.splitlines():
        if line.strip().startswith("```"):
            flush_buffer()
            in_code_block = not in_code_block
            translated_body.append(line)
            continue
        if in_code_block:
            translated_body.append(line)
        else:
            buffer.append(line)

    flush_buffer()
    translated_body = "\n".join(translated_body)

    yaml_content = yaml.safe_dump(front_matter, allow_unicode=True, sort_keys=True)
    output_content = f"---\n{yaml_content}---\n{translated_body}"

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"✅ Translated/Updated: {filename}")


if __name__ == "__main__":
    files = [f for f in os.listdir(SRC_DIR) if f.endswith(".md")]
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(process_file, files)

    print("\n🎉 Spanish posts updated successfully (only changed parts retranslated)")
