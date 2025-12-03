import os
import re
from datetime import datetime, timedelta

POSTS_DIR = "_posts"

# 全ポストの日時を記録して重複検出
used_dates = set()

def parse_front_matter(content):
    """
    Front matter をパースして (frontmatter_dict, body, raw_fm_text) を返す
    """
    if not content.startswith("---"):
        return None, content, None
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content, None
    
    fm_text = parts[1].strip()
    body = parts[2]

    fm = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    
    return fm, body, fm_text

def generate_unique_datetime(base_dt):
    """
    base_dt が使用済みなら秒単位で +1してユニークにする
    """
    new_dt = base_dt
    while new_dt in used_dates:
        new_dt = new_dt + timedelta(seconds=1)
    used_dates.add(new_dt)
    return new_dt

def process_post(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        original = f.read()

    fm, body, fm_text = parse_front_matter(original)
    if fm is None:
        print(f"[SKIP] Front matter がありません: {filepath}")
        return

    # ファイル名から日付抽出
    filename = os.path.basename(filepath)
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})-", filename)
    if not m:
        print(f"[ERROR] ファイル名に日付がありません: {filename}")
        return

    y, mo, d = map(int, m.groups())
    default_dt = datetime(y, mo, d, 0, 0, 0)

    # date: がある場合
    if "date" in fm:
        raw_date = fm["date"]

        # 時刻がない場合 例: "2024-11-20"
        if re.match(r"^\d{4}-\d{2}-\d{2}$", raw_date):
            base_dt = datetime.strptime(raw_date, "%Y-%m-%d")
        else:
            # 時刻付きはそのまま読み込み
            try:
                base_dt = datetime.fromisoformat(raw_date.replace(" +0900", ""))
            except:
                # 解析できない場合はファイル名の日付を使う
                base_dt = default_dt
    else:
        # date がない → ファイル名の日付を使用
        fm["date"] = default_dt.isoformat()
        base_dt = default_dt

    # 重複回避
    unique_dt = generate_unique_datetime(base_dt)

    # front matter を最新状態に反映
    fm["date"] = unique_dt.strftime("%Y-%m-%d %H:%M:%S +0900")

    # 新しいフロントマター生成
    new_fm = "---\n"
    for k, v in fm.items():
        new_fm += f"{k}: {v}\n"
    new_fm += "---\n"

    new_content = new_fm + body

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"[OK] 更新: {filepath} → {fm['date']}")

def main():
    print("▶ _posts の date を自動修正・ユニーク化します\n")

    for root, dirs, files in os.walk(POSTS_DIR):
        for file in files:
            if file.endswith(".md"):
                process_post(os.path.join(root, file))

    print("\n✔ 完了しました！すべての date がユニークになりました。")
    print("✔ jekyll build を実行するとページ3の問題は解決します。\n")

if __name__ == "__main__":
    main()
