import os
import yaml
import re
from deep_translator import GoogleTranslator

SRC_DIR = "_posts"
DEST_DIR = os.path.join("en", "_posts")
CACHE_FILE = "translation_cache.yaml"

os.makedirs(DEST_DIR, exist_ok=True)

translator = GoogleTranslator(source='ja', target='en')

# --------------------------------------------------------
# 正規化（キャッシュキーの安定化）
# --------------------------------------------------------
def normalize_key(text):
    if text is None:
        return ""
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)       # 空白正規化
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("”", '"').replace("“", '"')
    text = re.sub(r'[「」『』]', '"', text)
    return text

def normalize_quotes(text):
    if text is None:
        return ""
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("”", '"').replace("“", '"')
    text = re.sub(r'[「」『』]', '"', text)
    return text


# --------------------------------------------------------
# キャッシュ読み込み
# --------------------------------------------------------
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        translation_cache = yaml.safe_load(f) or {}
else:
    translation_cache = {}


def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(translation_cache, f, allow_unicode=True)


# --------------------------------------------------------
# 翻訳（段落単位 / キャッシュ付き / エラー処理）
# --------------------------------------------------------
def translate_paragraph(text):
    raw = text.rstrip("\n")
    stripped = raw.strip()

    if not stripped:
        return text  # 空行

    # コードブロック内は翻訳しない
    if stripped.startswith("```") or stripped.startswith("~~~"):
        return text
    if "<iframe" in stripped:
        return text

    key = normalize_key(stripped)

    # キャッシュヒット
    if key in translation_cache:
        return translation_cache[key] + ("\n" if text.endswith("\n") else "")

    # 翻訳
    try:
        result = translator.translate(stripped)
        if result is None:
            result = "[[ERROR]]"
        result = normalize_quotes(result)
    except Exception as e:
        print(f"⚠️ Translation failed: {e}")
        result = "[[ERROR]]"

    # キャッシュ保存
    translation_cache[key] = result

    return result + ("\n" if text.endswith("\n") else "")


# --------------------------------------------------------
# front matter 分離
# --------------------------------------------------------
def split_front_matter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content


# --------------------------------------------------------
# 本文翻訳（コードブロック言語指定含むすべて対応）
# --------------------------------------------------------
def translate_body(body):
    out = []
    in_code = False

    for line in body.splitlines(True):
        stripped = line.strip()

        # ``` や ~~~ で始まるコードブロック開始/終了
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = not in_code
            out.append(line)
            continue

        # コードブロック中はそのまま
        if in_code:
            out.append(line)
            continue

        # 翻訳
        out.append(translate_paragraph(line))

    return "".join(out)


# --------------------------------------------------------
# メイン処理
# --------------------------------------------------------
for filename in os.listdir(SRC_DIR):
    if not filename.endswith(".md"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    fm, body = split_front_matter(src_content)
    front = yaml.safe_load(fm) or {}

    # 差分チェック（高速）
    old_body = ""
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            old = f.read()
        _, old_body = split_front_matter(old)

    if normalize_key(old_body) == normalize_key(body):
        print(f"⏭️ No changes: {filename}")
        continue

    print(f"🔁 Updating: {filename}")

    # タイトル翻訳
    if "title" in front and front["title"]:
        key = normalize_key(front["title"])
        if key in translation_cache:
            front["title"] = translation_cache[key]
        else:
            try:
                t = translator.translate(front["title"])
                t = normalize_quotes(t if t else "[[ERROR]]")
                translation_cache[key] = t
                front["title"] = t
            except:
                front["title"] = "[[ERROR]]"

    front["lang"] = "en"

    # 本文翻訳
    translated_body = translate_body(body)

    # 書き出し
    output = f"---\n{yaml.safe_dump(front, allow_unicode=True)}---\n{translated_body}"

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ Done: {filename}\n")


save_cache()
print("🎉 Finished translation (stable fast version)")
