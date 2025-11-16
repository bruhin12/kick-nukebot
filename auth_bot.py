import os
import urllib.parse
from dotenv import load_dotenv

# Wymuszenie ręcznego załadowania .env z pełnej ścieżki
env_path = os.path.join(os.getcwd(), ".env")
print(f"[DEBUG] Loading .env from: {env_path}")

load_dotenv(env_path)

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")

print(f"CLIENT_ID: {CLIENT_ID}")
print(f"REDIRECT_URI: {REDIRECT_URI}")

if CLIENT_ID is None or REDIRECT_URI is None:
    print("[AUTH ERROR] Brak CLIENT_ID lub REDIRECT_URI w .env!")
    exit(1)

# Poprawny endpoint OAuth Kick
BASE = "https://id.kick.com/oauth/authorize"

SCOPES = [
    "user:read",
    "chat:read",
    "chat:write",
    "moderation:write",
    "events:subscribe"
]

def generate_oauth_link():
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": " ".join(SCOPES)
    }

    url = BASE + "?" + urllib.parse.urlencode(params)
    
    print("=== TWÓJ LINK OAUTH ===")
    print(url)
    print("WEJDŹ W TEN LINK JAKO BOT!")
    return url

if __name__ == "__main__":
    generate_oauth_link()
