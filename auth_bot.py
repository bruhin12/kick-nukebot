import os
from urllib.parse import urlencode

print("[AUTH] Start generowania linku OAuth...")

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")

if not CLIENT_ID or not REDIRECT_URI:
    print("[AUTH ERROR] CLIENT_ID lub REDIRECT_URI są puste!")
    print("CLIENT_ID:", CLIENT_ID)
    print("REDIRECT_URI:", REDIRECT_URI)
    exit(1)

params = {
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "response_type": "code",
    "scope": "chat:write chat:read user:profile",
}

oauth_url = "https://kick.com/oauth/authorize?" + urlencode(params)

print("\n===============================\n")
print("[AUTH] 🔗 Twój link OAuth:")
print(oauth_url)
print("\n===============================\n")
print("[AUTH] Wejdź w ten link jako BOT i zatwierdź aplikację.")
