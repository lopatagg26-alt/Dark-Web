
from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

PLATFORMS = {
    "TikTok": "https://www.tiktok.com/@{}",
    "Telegram": "https://t.me/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "YouTube": "https://www.youtube.com/@{}",
    "Reddit": "https://www.reddit.com/user/{}/"
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    username = request.args.get("username", "").strip()
    username = username.lstrip("@")

    if not re.fullmatch(r"[a-zA-Z0-9_.-]{1,50}", username):
        return jsonify({
            "error": "Некорректный username"
        }), 400

    results = []

    for platform, url in PLATFORMS.items():
        results.append({
            "platform": platform,
            "url": url.format(username)
        })

    return jsonify({
        "username": username,
        "results": results
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
