import os
import urllib.parse
from dotenv import load_dotenv

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

# kodowanie redirect_uri
redirect_encoded = urllib.parse.quote(REDIRECT_URI, safe='')

# SCOPES
scopes = "user:read chat:read chat:write moderation:write events:subscribe"
scopes_encoded = urllib.parse.quote(scopes, safe='')

# NOWY poprawny URL autoryzacji
auth_url = (
    f"https://id.kick.com/oauth/authorize?"
    f"response_type=code&"
    f"client_id={CLIENT_ID}&"
    f"redirect_uri={redirect_encoded}&"
    f"scope={scopes_encoded}"
)

print("=== TWÓJ LINK OAUTH ===")
print(auth_url)
print("WEJDŹ W TEN LINK JAKO BOT!")
