import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the Google Generative AI API key
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = gemini_api_key)

# Initialize the Gemini model
gemini_model = genai.GenerativeModel("gemini-2.0-flash")


def get_empathy_reply(user_msg):
    prompt = f"""
You are a Christian counselor chatbot. 
When someone shares an emotion or a thought, respond with empathy and heartfelt encouragement. 
Do NOT suggest Bible verses yet. Just show emotional support in a compassionate and hopeful tone.

User: {user_msg}
Response:
"""
    print("[Gemini] Empathy Prompt Sent:\n", prompt)
    response = gemini_model.generate_content(prompt)
    print("[Gemini] Empathy Response Received:\n", response.text.strip())
    return response.text.strip()


def get_verse_references(user_msg):
    prompt = f"""
You are a Christian counselor chatbot. 
Based on the user's concern, suggest 1 to 3 relevant Bible verse references that offer encouragement and hope. 
Only return the references from the *WEB (World English Bible)*, without any verse text.

Respond in this format:  
Isaiah 41:10, Romans 8:38–39

User: {user_msg}
References:
"""
    print("[Gemini] Reference Prompt Sent:\n", prompt)
    response = gemini_model.generate_content(prompt)
    print("[Gemini] Verse References Received:\n", response.text.strip())
    return response.text.strip()