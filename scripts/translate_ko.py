import os
import re
import yaml
import hashlib
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from deep_translator import GoogleTranslator

# ---------------------------------------------
# CONFIG
# ---------------------------------------------
WORKSPACE = os.getcwd()
SRC_DIR = os.path.join(WORKSPACE, "_posts")
DEST_DIR = os.path.join(WORKSPACE, "ko", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

CACHE_FILE = os.path.join(WORKSPACE, "translation_cache_ko.json")
MAX_WORKERS = 8
RETRY_COUNT = 2
RETRY_DELAY = 0.5  # seconds between retries

translator = GoogleTranslator(source='ja', target='ko')

# ---------------------------------------------
# キャッシュ読み込み（存在しなくても問題ない）
# ---------------------------------------------
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            TRANSLATION_CACHE = json.load(f)
    except Exception:
        TRANSLATION_CACHE = {}
else:
    TRANSLATION_CACHE = {}

# ---------------------------------------------
# 除外パターン（翻訳から完全に保護するブロック）
# - NOTE: mermaid はここに入れない（中を解析して翻訳する）
# ---------------------------------------------
EXCLUDE_BLOCK_PATTERNS = [
    # style / script / table / iframe / fenced code (``` ``` / ~~~ ~~~)
    (r"<style[\s\S]*?</style>", "STYLE"),
    (r"<script[\s\S]*?</script>", "SCRIPT"),
    (r"<table[\s\S]*?</table>", "TABLE"),
    (r"<iframe[\s\S]*?</iframe>", "IFRAME"),
    # fenced code blocks: ```lang ... ```  または ~~~lang ... ~~~
    (r"```[\w\-]*[\s\S]*?```", "CODE_FENCE"),
    (r"~~~[\w\-]*[\s\S]*?~~~", "CODE_FENCE2"),
]

# Compile flags
COMPILED_PATTERNS = [(re.compile(pat, re.IGNORECASE | re.DOTALL), tag) for pat, tag in EXCLUDE_BLOCK_PATTERNS]

# ---------------------------------------------
# ユーティリティ: ブロック抽出（重なり対処）
# - 全パターンのマッチ位置を収集して、後ろから置換する方式で安全に置換
# ---------------------------------------------
def extract_excluded_blocks(text):
    matches = []
    for pat, tag in COMPILED_PATTERNS:
        for m in pat.finditer(text):
            matches.append((m.start(), m.end(), m.group(0), tag))
    # ソートして後ろから置換（インデックスずれ防止）
    matches.sort(key=lambda x: x[0])
    placeholders = {}
    new_text = text
    offset = 0
    for i, (s, e, block, tag) in enumerate(matches):
        ph = f"__EXCL_{tag}_{i}__"
        # adjust for previous replacements
        s_adj = s + offset
        e_adj = e + offset
        new_text = new_text[:s_adj] + ph + new_text[e_adj:]
        placeholders[ph] = block
        offset += len(ph) - (e - s)
    return new_text, placeholders

def restore_excluded_blocks(text, placeholders):
    # 単純置換で戻す（placeholder はユニーク）
    for ph, block in placeholders.items():
        text = text.replace(ph, block)
    return text

# ---------------------------------------------
# 翻訳ラッパー（キャッシュ付き・リトライ・None安全）
# ---------------------------------------------
def cached_translate(text: str) -> str:
    # キーは text そのものの MD5
    key = hashlib.md5(text.encode("utf-8")).hexdigest()
    if key in TRANSLATION_CACHE:
        return TRANSLATION_CACHE[key]
    # 防御: 空文字はそのままキャッシュして返す
    if text.strip() == "":
        TRANSLATION_CACHE[key] = text
        return text
    # リトライ
    last_exc = None
    for attempt in range(1, RETRY_COUNT + 2):  # 1 + RETRY_COUNT attempts
        try:
            translated = translator.translate(text)
            if not translated:
                translated = text
            TRANSLATION_CACHE[key] = translated
            return translated
        except Exception as e:
            last_exc = e
            time.sleep(RETRY_DELAY)
    # 失敗時は元文をキャッシュして返す
    TRANSLATION_CACHE[key] = text
    print(f"[WARN] translation failed, cached original. snippet: {text[:60]!r}, error: {last_exc}")
    return text

# ---------------------------------------------
# Mermaid 行の翻訳 (コメントとラベルを無条件翻訳)
# ---------------------------------------------
def translate_mermaid_line(line: str) -> str:
    # コメント行 '%% comment'
    def repl_comment(m):
        return "%% " + cached_translate(m.group(1))
    line = re.sub(r"%%\s*(.*)", repl_comment, line)

    # ノードラベル・キャプション等を無条件翻訳
    patterns = [
        r'(\[)(.*?)(\])',      # [label]
        r'(\()([^()]*)(\))',   # (label)
        r'(\(\()([^()]*)(\)\))', # ((label))
        r'(\|)(.*?)(\|)',      # |label|
    ]
    for pat in patterns:
        line = re.sub(pat, lambda m: f"{m.group(1)}{cached_translate(m.group(2))}{m.group(3)}", line)
    return line

# ---------------------------------------------
# front matter 分離
# ---------------------------------------------
def split_front_matter(content: str):
    if content.startswith("---"):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", content

def load_yaml_safe(fm: str):
    try:
        return yaml.safe_load(fm) or {}
    except Exception:
        return {}

def extract_slug(filename: str) -> str:
    base = os.path.splitext(filename)[0]
    base = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', base)
    slug = re.sub(r'[^\w]+', '-', base)
    return slug.lower().strip('-')

# ---------------------------------------------
# 個別記事翻訳 (主要処理)
# ---------------------------------------------
def translate_article(filename: str) -> str:
    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)
    try:
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"[ERROR] cannot read {src_path}: {e}")
        return filename

    # 1) 除外ブロックを退避（iframe / code fences / style / script / table）
    tmp, placeholders = extract_excluded_blocks(content)

    # 2) front matter と body を分離
    fm, body = split_front_matter(tmp)
    fm_dict = load_yaml_safe(fm)

    # 3) front matter の title は翻訳。ただし他はそのまま保持
    if fm_dict.get("title"):
        try:
            fm_dict["title"] = cached_translate(str(fm_dict["title"]))
        except Exception:
            pass

    slug = extract_slug(filename)
    fm_dict["lang"] = "ko"
    fm_dict["permalink"] = f"/ko/{slug}/"

    # 4) 本文翻訳：Mermaid ブロックはノード単位で翻訳（div mermaid の中身をチェック）
    translated_lines = []
    in_code = False
    in_mermaid = False

    for line in body.splitlines():
        # フェンス行の判定（バックティック系）
        if line.strip().startswith("```") or line.strip().startswith("~~~"):
            in_code = not in_code
            translated_lines.append(line)
            continue
        if in_code:
            # code fence 中は翻訳しない（抜き出し済みの fenced code もあるが二重保護）
            translated_lines.append(line)
            continue

        # Mermaid start detection: "graph" or "flowchart" 行、または <div class="mermaid"> を含む場合
        trimmed = line.strip().lower()
        if trimmed.startswith("graph") or trimmed.startswith("flowchart") or "class=\"mermaid\"" in line.lower() or "class='mermaid'" in line.lower():
            in_mermaid = True
            translated_lines.append(line)
            continue

        if in_mermaid:
            # mermaid ブロック終端は空行または div close を検出（HTMLと混在の場合を包括）
            if trimmed == "" or trimmed == "</div>":
                if trimmed == "</div>":
                    in_mermaid = False
                translated_lines.append(line)
                continue
            # mermaid 内行はノード単位で翻訳
            translated_lines.append(translate_mermaid_line(line))
            continue

        # 通常行は無条件で翻訳（空行はキャッシュに保存されるが問題なし）
        translated_lines.append(cached_translate(line))

    translated_body = "\n".join(translated_lines)

    # 5) front matter を YAML に戻して、退避していた除外ブロックを復元
    final = f"---\n{yaml.safe_dump(fm_dict, allow_unicode=True)}---\n{translated_body}"
    final = restore_excluded_blocks(final, placeholders)

    # 6) ファイル書き込み（存在しないディレクトリは作る）
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(final)
        print(f"✅ Translated: {filename} -> {os.path.abspath(dest_path)} ({len(final)} bytes)")
    except Exception as e:
        print(f"[ERROR] failed to write {dest_path}: {e}")

    return filename

# ---------------------------------------------
# 並列実行エントリ
# ---------------------------------------------
def main():
    # sanity checks
    if not os.path.exists(SRC_DIR):
        print(f"[ERROR] SRC_DIR not found: {SRC_DIR}")
        return

    md_files = [f for f in os.listdir(SRC_DIR) if f.endswith(".md")]
    print(f"🔄 Translating {len(md_files)} articles with {MAX_WORKERS} workers...")
    if not md_files:
        print("[WARN] No markdown files found in _posts. Exiting.")
        return

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(translate_article, f): f for f in md_files}
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"[ERROR] processing {futures[future]}: {e}")

    # キャッシュ保存（並列後）
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(TRANSLATION_CACHE, f, ensure_ascii=False, indent=2)
        print(f"\n🎉 All translations done. Cache size: {len(TRANSLATION_CACHE)} entries -> {CACHE_FILE}")
    except Exception as e:
        print(f"[ERROR] failed to save cache: {e}")
