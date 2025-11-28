#!/usr/bin/env python3
import os
import yaml
import re
import time
import json
import hashlib
import threading
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from deep_translator import GoogleTranslator
from difflib import unified_diff
from functools import lru_cache

# ----------------------------
# Config
# ----------------------------
SRC_DIR = "_posts"
DEST_DIR = os.path.join("ko", "_posts")
os.makedirs(DEST_DIR, exist_ok=True)

CACHE_FILE = "translation_cache_ko.json"
MAX_WORKERS = 5                  # スレッド数（ファイル並列）
MAX_CONCURRENT_API = 2           # 同時API呼び出し数（重要：低めに）
API_RETRIES = 4                  # 1行当たりのリトライ回数
RETRY_BACKOFF = 0.6              # リトライ待機秒（指数的に増える）

# ログ
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# ----------------------------
# Translator helper (thread-local)
# ----------------------------
_thread_local = threading.local()

def get_translator():
    if not hasattr(_thread_local, "translator"):
        _thread_local.translator = GoogleTranslator(source='ja', target='ko')
    return _thread_local.translator

# ----------------------------
# Load/save cache
# ----------------------------
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            TRANSLATION_CACHE = json.load(f)
    except Exception:
        TRANSLATION_CACHE = {}
else:
    TRANSLATION_CACHE = {}

cache_lock = threading.Lock()

# ----------------------------
# Exclude block patterns (compiled)
# ----------------------------
EXCLUDE_BLOCK_PATTERNS = [
    (re.compile(r"<style[\s\S]*?</style>", re.MULTILINE), "STYLE"),
    (re.compile(r"<script[\s\S]*?</script>", re.MULTILINE), "SCRIPT"),
    (re.compile(r"<table[\s\S]*?</table>", re.MULTILINE), "TABLE"),
    (re.compile(r"<iframe[\s\S]*?</iframe>", re.MULTILINE), "IFRAME"),
    (re.compile(r"<div[^>]*class=[\"']?mermaid[\"']?[^>]*>[\s\S]*?</div>", re.MULTILINE), "MERMAID"),
    (re.compile(r"```[\w]*[\s\S]*?```", re.MULTILINE), "CODEBLOCK"),
]

def extract_excluded_blocks(text):
    placeholders = {}
    idx = 0
    for pattern, tag in EXCLUDE_BLOCK_PATTERNS:
        for m in pattern.finditer(text):
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

# ----------------------------
# Markdown-like / URL / HTML detection (skip translation)
# ----------------------------
MD_LINK_RE = re.compile(r'^\s*\[.*\]\(.*\)\s*$')
IMG_RE = re.compile(r'^\s*!\[.*\]\(.*\)\s*$')
HTML_TAG_LINE_RE = re.compile(r'^\s*<[^>]+>.*$')
URL_RE = re.compile(r'https?://')
ONLY_SYMBOLS_RE = re.compile(r'^[\s\-\*\>\#\+\=\(\)\[\]\{\}\:\/\.\,]+$')

def should_skip_line_translation(line: str) -> bool:
    s = line.strip()
    if not s:
        return True
    if MD_LINK_RE.match(s) or IMG_RE.match(s):
        return True
    if HTML_TAG_LINE_RE.match(s):
        return True
    if URL_RE.search(s) and len(s) < 200:
        # URLを含む短い行は翻訳しない（リンクボタンなど）
        return True
    if ONLY_SYMBOLS_RE.match(s):
        return True
    return False

# ----------------------------
# Semaphore for throttling concurrent API calls
# ----------------------------
api_semaphore = threading.Semaphore(MAX_CONCURRENT_API)

# ----------------------------
# Caching + translate with retries and backoff
# ----------------------------
def translate_text_cached(text: str, translator=None) -> str:
    """
    - text: 原文（可能な限りそのままの文字列をキーにする）
    - translator: スレッドローカルの translator（なければ内部で取得）
    """
    if translator is None:
        translator = get_translator()

    if not isinstance(text, str):
        text = str(text)

    key = hashlib.md5(text.encode("utf-8")).hexdigest()

    # キャッシュ読み（スレッド安全）
    with cache_lock:
        if key in TRANSLATION_CACHE:
            return TRANSLATION_CACHE[key]

    # 翻訳を行うべきでない行はそのまま
    if should_skip_line_translation(text):
        with cache_lock:
            TRANSLATION_CACHE[key] = text
        return text

    # リトライループ（semaphore で同時API数を制限）
    backoff = RETRY_BACKOFF
    last_exception = None
    for attempt in range(1, API_RETRIES + 1):
        try:
            api_semaphore.acquire()
            try:
                # translate may raise; ensure returned string
                res = translator.translate(text)
            finally:
                api_semaphore.release()

            if res is None:
                res = text
            res = str(res)
            with cache_lock:
                TRANSLATION_CACHE[key] = res
            return res
        except Exception as e:
            last_exception = e
            logging.warning(f"Translate failed attempt {attempt}/{API_RETRIES} for text[:40]={text[:40]!r}: {e}")
            time.sleep(backoff)
            backoff *= 1.8
            # recreate translator object in case it got into bad state
            try:
                _thread_local.translator = GoogleTranslator(source='ja', target='ko')
                translator = _thread_local.translator
            except Exception:
                pass

    # 全部失敗した場合は原文をキャッシュして返す（次回は試さない）
    logging.error(f"Translate all attempts failed for text[:60]={text[:60]!r}, returning original")
    with cache_lock:
        TRANSLATION_CACHE[key] = text
    return text

# ----------------------------
# Mermaid patterns (compiled)
# ----------------------------
MERMAID_COMMENT_PATTERN = re.compile(r"%%\s*(.*)")
MERMAID_NODE_PATTERNS = [
    re.compile(r'(\[)(.*?)(\])'),
    re.compile(r'(\()([^()]*)(\))'),
    re.compile(r'(\(\()([^()]*)(\)\))'),
    re.compile(r'(\|)(.*?)(\|)'),
]

def translate_mermaid_line(line, translator):
    # コメント
    line = MERMAID_COMMENT_PATTERN.sub(lambda m: "%% " + translate_text_cached(m.group(1), translator), line)
    # ノードラベル
    for pat in MERMAID_NODE_PATTERNS:
        def repl(m):
            start, text, end = m.group(1), m.group(2), m.group(3)
            # 翻訳対象判定（日本語がある場合のみ翻訳）
            if re.search(r'[一-龯ぁ-んァ-ン]', text):
                return f"{start}{translate_text_cached(text, translator)}{end}"
            return m.group(0)
        line = pat.sub(repl, line)
    return line

# ----------------------------
# YAML / slug helpers
# ----------------------------
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

@lru_cache(maxsize=512)
def extract_slug(filename):
    base = os.path.splitext(filename)[0]
    base = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', base)
    slug = re.sub(r'[^\w]+', '-', base)
    return slug.lower().strip('-')

# ----------------------------
# Single file processing
# ----------------------------
def process_file(filename):
    src_path = os.path.join(SRC_DIR, filename)
    dest_path = os.path.join(DEST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()

    cleaned_body, placeholders = extract_excluded_blocks(src_content)
    fm, body = split_front_matter(cleaned_body)
    front_matter = load_yaml_safe(fm)

    # 差分チェック（既存翻訳が最新ならスキップ）
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            old = f.read()
        fm2, old_body = split_front_matter(old)
        diff = list(unified_diff(old_body.splitlines(), body.splitlines()))
        if not diff:
            return f"⏭️ No changes: {filename}"

    translator = get_translator()

    # front matter title
    if front_matter.get("title"):
        front_matter["title"] = translate_text_cached(front_matter["title"], translator)

    slug = extract_slug(filename)
    front_matter["lang"] = "ko"
    front_matter["permalink"] = f"/ko/{slug}/"

    translated_body = ""
    in_code_block = False
    in_mermaid_block = False

    for line in body.splitlines():
        stripped = line.strip()

        # コードブロックトグル
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            translated_body += line + "\n"
            continue
        if in_code_block:
            translated_body += line + "\n"
            continue

        # Mermaid start (we already excluded entire mermaid divs, but handle inline)
        if stripped.startswith("graph") or stripped.startswith("flowchart"):
            in_mermaid_block = True
            translated_body += line + "\n"
            continue
        if in_mermaid_block:
            if stripped == "</div>":
                in_mermaid_block = False
                translated_body += line + "\n"
            else:
                translated_body += translate_mermaid_line(line, translator) + "\n"
            continue

        # 普通行：翻訳（ただし短すぎる・リンクだけ・HTML行はスキップ）
        if should_skip_line_translation(line):
            translated_body += line + "\n"
        else:
            translated_body += translate_text_cached(line, translator) + "\n"

    final_output = restore_excluded_blocks(
        f"---\n{yaml.safe_dump(front_matter, allow_unicode=True)}---\n{translated_body}",
        placeholders
    )

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_output)

    return f"✅ Translated: {filename}"

# ----------------------------
# Main: parallel execution + save cache
# ----------------------------
if __name__ == "__main__":
    files = [f for f in os.listdir(SRC_DIR) if f.endswith(".md")]
    logging.info(f"Starting translation of {len(files)} files with {MAX_WORKERS} workers (API concurrency={MAX_CONCURRENT_API})")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(process_file, fn): fn for fn in files}
        for future in as_completed(futures):
            try:
                logging.info(future.result())
            except Exception as e:
                logging.exception("Error processing file")

    # save cache
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(TRANSLATION_CACHE, f, ensure_ascii=False, indent=2)
        logging.info(f"Saved cache ({len(TRANSLATION_CACHE)} entries) to {CACHE_FILE}")
    except Exception as e:
        logging.exception("Failed to save cache")

    logging.info("All done.")
