# Netlify ZIP Deploy Script

This Python script allows you to deploy a local folder to a Netlify site using the Netlify REST API.  
It packages the folder into a `.zip` file and uploads it directly to the target site, **without** requiring `node.js` or `netlify-cli`.

## ✨ Features

- No need for `node.js`, `npm`, or `netlify-cli`
- Fully automated ZIP packaging and upload
- Supports both draft (`preview`) and production deployment
- Logs progress to the console for transparency
- Includes `check_ascii_filenames_in_folder.py` — a helper script to scan for non-ASCII filenames before deployment.

## 🛠 Requirements

- Python 3.6+
- `requests` library (`pip install requests`)
- A [Netlify Personal Access Token](https://app.netlify.com/user/applications)
- Your Netlify Site ID (Project ID)

## 📦 Setup

1. Clone or download this repository.
2. Edit `netlify_deploy.py` and set:

```python
FOLDER_TO_UPLOAD = "path/to/your/site"
ACCESS_TOKEN = "your_netlify_token"
SITE_ID = "your_netlify_site_id"
```

3. Run the script:

```bash
python netlify_deploy.py
```

## 🚀 Example Output

```
📦 ZIP作成中: ./site → deploy.zip
✅ ZIP作成完了

🚀 Netlifyにデプロイ開始（production=True）
➡ アップロード先: https://api.netlify.com/api/v1/sites/...
📤 アップロード中（3,285バイト）...
✅ デプロイ成功！
🔗 https://your-site.netlify.app
```

## 🔐 Security Note

Do **not** commit your access token to public repositories.  
Use environment variables or `.env` files for safer token management.

## 👤 Author

- **7M4MON**
- 📅 July 5, 2025

## 🪪 License

MIT License
