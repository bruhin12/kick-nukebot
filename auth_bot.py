import os
from dotenv import load_dotenv
from urllib.parse import urlencode

env_path = os.path.join(os.getcwd(), ".env")
print(f"[DEBUG] Loading .env from: {env_path}")

load_dotenv(env_path)

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")

if not CLIENT_ID or not REDIRECT_URI:
    print("[AUTH ERROR] Brak CLIENT_ID lub REDIRECT_URI w .env!")
    print("CLIENT_ID:", CLIENT_ID)
    print("REDIRECT_URI:", REDIRECT_URI)
    exit(1)

params = {
    "response_type": "code",
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "scope": "user:read chat:read chat:write moderation:write events:subscribe"
}

oauth_url = (
    "https://accounts.kick.com/oauth2/authorize"
    f"?response_type=code"
    f"&client_id={CLIENT_ID}"
    f"&redirect_uri={REDIRECT_URI}"
    f"&scope=user:read chat:read chat:write moderation:write events:subscribe"
)


print("=== TWÓJ LINK OAUTH ===")
print(oauth_url)
print("WEJDŹ W TEN LINK JAKO BOT!")

