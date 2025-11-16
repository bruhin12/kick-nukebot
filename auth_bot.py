import os
from dotenv import load_dotenv
from urllib.parse import quote

# 🔧 Wymuszenie poprawnej ścieżki do .env
env_path = os.path.join(os.getcwd(), ".env")
print(f"[DEBUG] Loading .env from: {env_path}")
load_dotenv(env_path)

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")

print("CLIENT_ID:", CLIENT_ID)
print("REDIRECT_URI:", REDIRECT_URI)

if not CLIENT_ID or not REDIRECT_URI:
    print("[AUTH ERROR] Brak CLIENT_ID lub REDIRECT_URI w .env!")
    exit(1)

# 🔥 UWAGA: poprawny endpoint OAuth Kick
OAUTH_URL = (
    "https://id.kick.com/oauth/authorize"
    "?response_type=code"
    f"&client_id={quote(CLIENT_ID)}"
    f"&redirect_uri={quote(REDIRECT_URI)}"
    "&scope=user:read chat:read chat:write moderation:write events:subscribe"
)

print("=== TWÓJ POPRAWNY LINK OAUTH ===")
print(OAUTH_URL)
print("WEJDŹ W TEN LINK JAKO BOT!")
