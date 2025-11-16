import os
from urllib.parse import urlencode
from dotenv import load_dotenv

# Wymuszenie ścieżki .env
env_path = os.path.join(os.getcwd(), ".env")
print(f"[DEBUG] Loading .env from: {env_path}")
load_dotenv(env_path)

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")

print(f"CLIENT_ID: {CLIENT_ID}")
print(f"REDIRECT_URI: {REDIRECT_URI}")

if not CLIENT_ID or not REDIRECT_URI:
    print("[AUTH ERROR] Brak CLIENT_ID lub REDIRECT_URI w .env!")
    exit(1)

# Kick OAuth endpoint – JEDYNY poprawny
OAUTH_URL = "https://id.kick.com/oauth/authorize"

params = {
    "response_type": "code",
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "scope": "user:read chat:read chat:write moderation:write events:subscribe"
}

final_url = f"{OAUTH_URL}?{urlencode(params)}"

print("=== TWÓJ LINK OAUTH ===")
print(final_url)
print("WEJDŹ W TEN LINK JAKO BOT!")
