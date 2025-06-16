import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Replace with your actual env var name
BOT_TOKEN = os.getenv("JBIBLECHAT_TELEGRAM")  # or hardcode it if testing
WEBHOOK_URL = "https://bible-chatbot.onrender.com/telegram"

# Set the webhook
response = requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook",
    params={"url": WEBHOOK_URL}
)

print("[Webhook Setup] Status:", response.status_code)
print("[Webhook Setup] Response:", response.json())