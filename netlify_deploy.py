# ------------------------------------------------------------------------------
# File: netlify_deploy.py
# Purpose: Uploads a specified local folder to Netlify via REST API as a ZIP file.
# Author: 7M4MON
# Date: 2025-07-05
# ------------------------------------------------------------------------------

import requests
import os
import zipfile

def zip_folder(folder_path, zip_path):
    print(f"📦 ZIP作成中: {folder_path} → {zip_path}")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
                # print(f"  - 追加: {arcname}")
    print("✅ ZIP作成完了\n")

def deploy_to_netlify(folder_path, access_token, site_id, production=False):
    zip_path = "deploy.zip"

    # ZIPを作成
    zip_folder(folder_path, zip_path)

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/zip"
    }

    params = {"prod": str(production).lower()}
    url = f"https://api.netlify.com/api/v1/sites/{site_id}/deploys"

    print(f"🚀 Netlifyにデプロイ開始（production={production}）")
    print(f"➡ アップロード先: {url}")

    with open(zip_path, "rb") as f:
        binary_data = f.read()
        print(f"📤 アップロード中（{len(binary_data)}バイト）...")
        response = requests.post(url, headers=headers, params=params, data=binary_data)

    # os.remove(zip_path)
    print("🧹 ZIP削除（スキップ中）")

    if response.status_code == 200:
        deploy_url = response.json().get("deploy_ssl_url", "URL not found")
        print(f"✅ デプロイ成功！\n🔗 {deploy_url}")
    else:
        print("❌ デプロイ失敗")
        print(f"ステータスコード: {response.status_code}")
        print(f"レスポンス: {response.text}")

# === 設定 ===
FOLDER_TO_UPLOAD = "xxxxxxxxxxx"  # アップロードしたいフォルダ
ACCESS_TOKEN = "nfp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # トークン（※本番では環境変数が推奨）
SITE_ID = "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"  # NetlifyのサイトID

# 実行
deploy_to_netlify(FOLDER_TO_UPLOAD, ACCESS_TOKEN, SITE_ID, production=True)
