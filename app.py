from flask import Flask, request, Response
# If these are your own functions, import from a local module (e.g., telegram_utils.py)
from telegram_utils import process_telegram_update, send_msg
import os

app = Flask(__name__)

@app.route("/telegram", methods=['POST'])
def telegram_webhook():
    update = request.get_json()
    process_telegram_update(update)
    return 'OK', 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)