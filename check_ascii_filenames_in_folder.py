# ------------------------------------------------------------------------------
# File: check_ascii.py
# Purpose: Scans a given folder and lists files or directories that contain
#          non-ASCII (e.g., Japanese) characters in their names.
# Author: 7M4MON
# Date: 2025-07-05
# ------------------------------------------------------------------------------

import os
import re

# 日本語などの非ASCII文字を検出する正規表現
non_ascii_pattern = re.compile(r'[^\x00-\x7F]')

def find_non_ascii_paths(root_dir):
    print(f"🔍 Scanning '{root_dir}' for non-ASCII file/folder names...\n")

    found = False
    for root, dirs, files in os.walk(root_dir):
        # チェック対象：ディレクトリ名とファイル名
        for name in dirs + files:
            if non_ascii_pattern.search(name):
                full_path = os.path.join(root, name)
                print(f"⚠️ 非ASCII名: {full_path}")
                found = True

    if not found:
        print("✅ 全てのファイルとフォルダはASCII名です。安全です！")

# チェックしたいフォルダを指定（例："dist"）
target_directory = "D:/DM_H110/hp"
find_non_ascii_paths(target_directory)
