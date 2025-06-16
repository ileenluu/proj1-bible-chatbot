import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Get Telegram bot token from environment
BOT_TOKEN = os.getenv("JBIBLECHAT_TELEGRAM")
WEBHOOK_URL = "https://bible-chatbot.onrender.com/telegram"

# Optional: Validate token exists
if not BOT_TOKEN:
    raise ValueError("Telegram bot token is missing. Check your environment variable 'JBIBLECHAT_TELEGRAM'.")

# Set the webhook
response = requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook",
    params={"url": WEBHOOK_URL}
)

# Print response for confirmation
print("[Webhook Setup] Status:", response.status_code)
print("[Webhook Setup] Response:", response.json())