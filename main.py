from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/..."  # replace with your real URL

@app.route('/tvwebhook', methods=['POST'])
def tvwebhook():
    data = request.json
    message = data.get("message", "No message provided.")
    requests.post(DISCORD_WEBHOOK_URL, json={"content": message})
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
