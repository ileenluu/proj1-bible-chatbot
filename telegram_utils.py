import requests
import os
from gemini_reply import get_gemini_reply

TELEGRAM_BOT_TOKEN = os.getenv("JBIBLECHAT_TELEGRAM")
BOT_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


def process_telegram_update(update):
    if "message" in update and "text" in update['message']:

    # Extract the chat ID and message text from the update
        chat_id = update['message']['chat']['id']
        message_id = update['message']['message_id']
        user_msg = update['message']['text']
        print(f"[RECEIVED] Chat ID: {chat_id}, Message ID: {message_id}")

        if user_msg == '/start':
            response = "Hello Beloved!"
        elif user_msg == '/end':
            response = 'Stay blessed! See you next time!'
        else:
            response_text = get_gemini_reply(user_msg)

    send_msg(chat_id, response_text)


def send_msg(chat_id, response_text):
    send_message_url = f"{BOT_URL}/sendMessage"
    requests.post(send_message_url, data={"chat_id": chat_id, "text": response_text})
