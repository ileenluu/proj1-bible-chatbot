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

    # Simple logic to detect if it's a question
    question_keywords = ("?", "why", "who", "when", "what", "where", "how")
    lowered_msg = user_msg.casefold().strip()

    # Check if the message contains any of the question indicators
    is_question = any(keyword in lowered_msg for keyword in question_keywords)

    if is_question:
        prompt = f"""
            You are a Christian pastor chatbot. 
            When someone asks a question about the Bible or faith, respond with a short, clear, and caring explanation.
            Important theological foundation to reflect in your answer:
            God's commandments (e.g., the Ten Commandments) reveal His perfect standard.
            They are not meant for humans to fulfill by their own efforts, but to show our need for a Savior. 
            Only Jesus Christ — who fulfilled the Law perfectly — can save us and make us righteous before God.
            Emphasize grace through faith in Christ, not salvation by works.
            Avoid heavy theological jargon. Keep the tone warm, respectful, and rooted in biblical truth.
            DO NOT include any Bible verses yet. Keep your tone warm, respectful, and hopeful — but also confident in truth.

            Question: {user_msg}
            Response:
        """

    else:
        prompt = f"""
            You are a Christian chatbot who speaks with strength, love, and faith.
            When someone shares their fears, sadness, or expresses their need for Jesus, 
            respond with affirming encouragement that reminds them of Jesus’s provision, strength and love.

            Do not act overly soft or protective — speak with loving confidence.
            Make them feel uplifted, capable, and deeply valued in Christ.
            Emphasize that they are not alone, and that Jesus walks with them in power and love.

            Do NOT include Bible verses yet. Focus on encouragement rooted in faith and strength.

            User: {user_msg}
            Response:
        """

    print("[Gemini] Prompt Sent:\n", prompt)
    response = gemini_model.generate_content(prompt)
    print("[Gemini] Response Received:\n", response.text.strip())
    return response.text.strip()


def get_verse_references(user_msg):
    prompt = f"""
        You are a Christian chatbot assistant.
        Based on the user's message below, suggest 1 to 3 relevant Bible verse references 
        that offer encouragement, clarity, or spiritual support which brings hope and peace to the user.
        Only return the references (e.g., "Romans 5:5", "Titus 2:13").
        Do NOT include any explanation or verse text.

        Respond in this format:  
        Isaiah 41:10, Romans 8:38–39

        Message: {user_msg}
        References:
    """
    print("[Gemini] Verse Reference Prompt Sent:\n", prompt)
    response = gemini_model.generate_content(prompt)
    print("[Gemini] Verse References Received:\n", response.text.strip())
    return response.text.strip()