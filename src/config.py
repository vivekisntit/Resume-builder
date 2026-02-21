from google import genai

def validate_api(api_key: str) -> bool:
    try:
        client = genai.Client(api_key=api_key)
        client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Test"
        )
        return True
    except Exception:
        return False