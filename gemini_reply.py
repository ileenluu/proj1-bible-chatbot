import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the Google Generative AI API key
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = gemini_api_key)


def get_gemini_reply(user_msg, version="WEB"):

    # Initialize the Google Gemini client
    gemini_model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    You are a Christian counselor chatbot. 
    When someone shares an emotion or a thought, reply with empathy and understanding, 
    and offer 1 to 3 bible verse(s) from the *{version}* version that bring(s) encouragement and hope. Keep it short and heartfelt.
    
    User: {user_msg}
    Response:
    """
    print("[Gemini] Prompt sent:\n", prompt)  # 🔍 Print the full prompt
    response = gemini_model.generate_content(prompt)
    print("[Gemini] Response received:\n", response.text.strip())  # 🔍 Print Gemini's reply
    return response.text.strip()