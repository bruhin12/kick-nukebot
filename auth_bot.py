import os
from dotenv import load_dotenv
import urllib.parse

env_path = os.path.join(os.getcwd(), ".env")
load_dotenv(env_path)

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
CLIENT_SECRET = os.getenv("KICK_CLIENT_SECRET")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")

print("CLIENT_ID:", CLIENT_ID)
print("REDIRECT_URI:", REDIRECT_URI)

if not CLIENT_ID or not REDIRECT_URI:
    print("[AUTH ERROR] BRAK danych OAuth!")
    exit(1)

base = "https://id.kick.com/oauth/authorize"

params = {
    "response_type": "code",
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "scope": "user:read chat:read chat:write moderation:write events:subscribe"
}

url = base + "?" + urllib.parse.urlencode(params)

print("=== TWÓJ LINK OAUTH ===")
print(url)
print("WEJDŹ W TEN LINK JAKO BOT!")
