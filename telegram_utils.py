from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import os
from gemini_reply import get_gemini_reply

TELEGRAM_BOT_TOKEN = os.getenv("JBIBLECHAT_TELEGRAM")
BOT_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

# Store user version preferences in memory (for production, use database)
user_versions = {}

def process_telegram_update(update):
    if "message" in update and "text" in update["message"]:
        chat_id = update["message"]["chat"]["id"]
        user_name = update["message"]["from"]["first_name"]
        user_msg = update["message"]["text"]
        print(f"[RECEIVED] Chat ID: {chat_id}, Message: {user_msg}")

        if user_msg == "/start":
            version = user_versions.get(chat_id)
            version_note = f"\n\n📖 You previously selected *{version.upper()}*. You can change it anytime below." if version else ""

            # Bible version selection buttons
            keyboard = [
                [InlineKeyboardButton("WEB", callback_data="set_version_WEB")],
                [InlineKeyboardButton("KJV", callback_data="set_version_KJV")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            send_msg(chat_id,
                f"✨ *Welcome {user_name}! Please choose your preferred Bible version:*\n"
                "📜 *KJV* - Classic Old English style\n"
                "📘 *WEB* - Clear and modern English"
                f"{version_note}",
                reply_markup)

        elif user_msg == "/end":
            response_text = f"Stay blessed {user_name}! See you next time!"
            send_msg(chat_id, response_text)

        else:
            # Use stored version or default to KJV
            version = user_versions.get(chat_id, "KJV")
            response_text = get_gemini_reply(user_msg, version)
            send_msg(chat_id, response_text)

    elif "callback_query" in update:
        process_callback_query(update)


# Handle button presses for version selection
def process_callback_query(update):
    query = update['callback_query']
    chat_id = query['message']['chat']['id']
    data = query['data']

    if data.startswith('set_version_'):
        version = data.split('_')[2]
        user_versions[chat_id] = version
        send_msg(chat_id, f"✅ Bible version set to: *{version.upper()}*. You can now ask your questions!")


def send_msg(chat_id, response_text, reply_markup=None):
    send_message_url = f"{BOT_URL}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": response_text,
        "parse_mode": "Markdown"
    }
    if reply_markup:
        data["reply_markup"] = reply_markup.to_json()
    response = requests.post(send_message_url, data=data)
    print("[SEND MSG] Status:", response.status_code)
    print("[SEND MSG] Response:", response.json())