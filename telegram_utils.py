import requests
import os
from gemini_reply import get_gemini_reply

TELEGRAM_BOT_TOKEN = os.getenv("JBIBLECHAT_TELEGRAM")
BOT_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def process_telegram_update(update):
    if "message" in update and "text" in update["message"]:
        chat_id = update["message"]["chat"]["id"]
        user_msg = update["message"]["text"]
        print(f"[RECEIVED] Chat ID: {chat_id}, Message: {user_msg}")

        if user_msg == "/start":
            response_text = "Hello Beloved!"
        elif user_msg == "/end":
            response_text = "Stay blessed! See you next time!"
        else:
            response_text = get_gemini_reply(user_msg)

        send_msg(chat_id, response_text)

def send_msg(chat_id, response_text):
    send_message_url = f"{BOT_URL}/sendMessage"
    response = requests.post(send_message_url, data={"chat_id": chat_id, "text": response_text})
    print("[SEND MSG] Status:", response.status_code)
    print("[SEND MSG] Response:", response.json())