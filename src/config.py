from openai import OpenAI, AuthenticationError

def validate_api(api_key: str) -> bool:
    try:
        client = OpenAI(api_key=api_key)
        client.models.list()
        return True
    except AuthenticationError:
        return False
