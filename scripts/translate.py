import os
import yaml
import re
import time
from deep_translator import GoogleTranslator
from difflib import unified_diff

# ===== 設定 =====
SRC_DIR = "_posts"
DEST_DIR = os.path.join("en", "_posts")
CACHE_FILE = "translation_cache.yaml"
os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='en')

# ===== キャッシュ管理 =====
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(cache, f, allow_unicode=True)

cache = load_cache()
save_interval = 50  # 50件翻訳ごとにキャッシュ保存
translate_count = 0


# ===== 正規化処理 =====
def normalize_quotes(text):
    if not text:
        return text
    text = re.sub(r'[“”‘’«»„‟‹›「」『』〝〞‚‛`´]', '"', text)
    text = re.sub(r'``(.*?)``', r'"\1"', text)
    text = re.sub(r"''(.*?)''", r'"\1"', text)
    text = re.sub(r"\b'(.*?)'\b", r'"\1"', text)
    return text


# ===== 翻訳関数（キャッシュ付き） =====
def translate_text(text):
    global translate_count

    text = text.strip()
    if not text or re.match(r"^```", text) or re.search(r'<iframe.*?</iframe>', text, re.DOTALL):
        return text

    # キャッシュチェック
    if text in cache:
        return cache[text]

    try:
        result = translator.translate(text)
        if result is None:
            print(f"⚠️ None returned for: {text[:30]}...")
            return text
        result = normalize_quotes(str(result))
        cache[text] = result
        translate_count += 1

        # 定期キャッシュ保存（安全のため）
        if translate_count % save_interval == 0:
            save_cache(cache)
            print(f"💾 Cache auto-saved ({translate_count} translations)")

        # API制限緩和（安定化）
        time.sleep(0.2)
        return result

    except Exception as e:
        print(f"⚠️ 翻訳失敗: {e}（スキップ）")
        return text


# ===== Front Matter 分離 =====
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content


def load_yaml_safe(fm):
    try:
        return yaml.safe_load(fm) or {}
    except yaml.YAMLError:
        return {}


# ===== メイン処理 =====
for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

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

    # ===== 差分翻訳処理 =====
    if old_body.strip():
        diff = list(unified_diff(old_body.splitlines(), body.splitlines()))
        if not diff:
            print(f"⏭️ No changes: {filename}")
            continue
        else:
            print(f"🔁 Diff detected: {filename} — 差分翻訳")

        new_lines = old_body.splitlines()
        body_lines = body.splitlines()
        for i in range(len(body_lines)):
            if i < len(new_lines):
                if body_lines[i] != new_lines[i]:
                    new_lines[i] = translate_text(body_lines[i])
            else:
                new_lines.append(translate_text(body_lines[i]))
        translated_body = "\n".join(new_lines)

    else:
        print(f"🆕 New file: {filename} — 全文翻訳")
        translated_body = ""
        in_code_block = False
        for line in body.splitlines():
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                translated_body += line + "\n"
            elif in_code_block:
                translated_body += line + "\n"
            else:
                translated_body += translate_text(line) + "\n"

    # ===== Front Matter 翻訳 =====
    if front_matter.get("title"):
        front_matter["title"] = translate_text(front_matter["title"])
    front_matter["lang"] = "en"

    # ===== 出力 =====
    output_content = f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}\n"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"✅ Translated/Updated: {filename}")

# ===== 最終キャッシュ保存 =====
save_cache(cache)
print("\n🎉 English posts updated successfully (diff-based, cached, long-run safe)")
