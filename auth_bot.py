import os
import urllib.parse
from dotenv import load_dotenv

# wczytanie .env z GitHub Actions
env_path = os.path.join(os.getcwd(), ".env")
print(f"[DEBUG] Loading .env from: {env_path}")
load_dotenv(env_path)

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")

print("CLIENT_ID:", CLIENT_ID)
print("REDIRECT_URI:", REDIRECT_URI)

def generate_oauth_link():
    if not CLIENT_ID or not REDIRECT_URI:
        print("[AUTH ERROR] Brak CLIENT_ID lub REDIRECT_URI!")
        return

    # ***** POPRAWNA DOMENA OAUTH *****
    base = "https://id.kick.com/oauth/authorize"

    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user:read chat:read chat:write moderation:write events:subscribe"
    }

    url = base + "?" + urllib.parse.urlencode(params)

    print("=== TWÓJ LINK OAUTH (DZIAŁA) ===")
    print(url)
    print("WEJDŹ W TEN LINK JAKO BOT!")
    return url


if __name__ == "__main__":
    generate_oauth_link()
