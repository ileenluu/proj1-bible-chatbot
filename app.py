from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from gemini_reply import get_gemini_reply
import os

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incomining_msg = request.form.get('Body', "")

    # Get the Gemini-generated reply
    try:
        gemini_response = get_gemini_reply(incomining_msg)
    except Exception as e:
        gemini_response = "Sorry, there was an error processing your request. Please try again later."

    # Crate Twilio Whatsapp response
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(gemini_response)

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)