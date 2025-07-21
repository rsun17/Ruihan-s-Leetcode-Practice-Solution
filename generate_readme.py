import os
import re

BASE_DIR = "."
DIFFICULTY_FOLDERS = {
    "easy": "Easy",
    "medium": "Medium",
    "hard": "Hard"
}
README_PATH = os.path.join(BASE_DIR, "README.md")

TABLE_HEADER = """\
# 🧠 Ruihan's LeetCode Practice Solutions

| # | Title | Difficulty | Tags | Solution |
|---|-------|------------|------|----------|
"""

rows = []

for folder, difficulty in DIFFICULTY_FOLDERS.items():
    folder_path = os.path.join(BASE_DIR, folder)
    if not os.path.exists(folder_path):
        continue

    for filename in sorted(os.listdir(folder_path)):
        if not filename.endswith(".py"):
            continue

        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        title_match = re.search(r"#\s*0*(\d+)\s+(.+?)\s+-\s+(Easy|Medium|Hard)", content, re.IGNORECASE)
        tags_match = re.search(r"#\s*Tags:\s*(.+)", content)

        if title_match:
            number = title_match.group(1).strip()
            title = title_match.group(2).strip()
            level = title_match.group(3).capitalize().strip()
            tags = tags_match.group(1).strip() if tags_match else ""
            rel_path = f"{folder}/{filename}"
            row = f"| {number} | {title} | {level} | {tags} | [Python]({rel_path}) |"
            rows.append(row)

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(TABLE_HEADER + "\n".join(rows) + "\n")
