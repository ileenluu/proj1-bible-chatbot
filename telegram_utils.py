import requests
import os
from gemini_reply import get_empathy_reply, get_verse_references
from web_bible_api import get_web_verse


TELEGRAM_BOT_TOKEN = os.getenv("JBIBLECHAT_TELEGRAM")
BOT_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


def process_telegram_update(update):
    if "message" in update and "text" in update["message"]:
        chat_id = update["message"]["chat"]["id"]
        user_name = update["message"]["from"]["first_name"]
        user_msg = update["message"]["text"]
        print(f"[RECEIVED] Chat ID: {chat_id}, Message: {user_msg}")

        if user_msg == "/start":
            welcome_text = (
                f"✨ Welcome to JBiblechat {user_name}!\n\n"
                "✨ *Note:* Our shared Bible verses are from the *WEB (World English Bible)* — "
                "a modern, public-domain translation. "
                "For deeper study, we encourage you to refer to your own preferred Bible version."
            )
            send_msg(chat_id, welcome_text)

        elif user_msg == "/end":
            bye_text = f"Stay blessed {user_name}! See you next time!"
            send_msg(chat_id, bye_text)

        else:
            # Get empathy response from Gemini
            empathy_text = get_empathy_reply(user_msg)

            # Get verse references from Gemini
            references = get_verse_references(user_msg)

            # Format and fetch verse texts
            verse_output = ""
            for ref in references.split(","):
                ref = ref.strip()
                verse_text = get_web_verse(ref)
                if verse_text:
                    verse_output += f"\n\n*{ref} (WEB)*\n{verse_text}"
                else:
                    verse_output += f"\n\n*{ref} (WEB)*\n⚠️ Verse not found."

            # Final combined response
            final_response = f"{empathy_text}\n\n{verse_output}"
            send_msg(chat_id, final_response)
        

def send_msg(chat_id, response_text):
    send_message_url = f"{BOT_URL}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": response_text,
        "parse_mode": "Markdown",
    }
    response = requests.post(send_message_url, data=data)
    print("[SEND MSG] Status:", response.status_code)
    print("[SEND_MSG] Response:", response.json())