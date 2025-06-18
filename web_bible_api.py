import requests

def get_web_verse(reference):
    """
    Fetch verse text from Bible-API using the WEB (World English Bible) version.
    Input: reference (e.g., "Isaiah 41:10")
    Output: clean verse text or error message
    """
    api_url = f"https://bible-api.com/{reference}?translation=web"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data.get("text", "").strip()
        else:
            return f"⚠️ Unable to fetch verse: {reference}."
    except Exception as e:
        return f"⚠️ Error retrieving {reference}: {str(e)}"
    