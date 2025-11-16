import os
import urllib.parse

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")

if not CLIENT_ID or not REDIRECT_URI:
    print("[AUTH ERROR] Brak CLIENT_ID lub REDIRECT_URI w .env!")
    print("CLIENT_ID:", CLIENT_ID)
    print("REDIRECT_URI:", REDIRECT_URI)
    exit(1)

# Generowanie linku OAuth Kick
base_url = "https://kick.com/oauth/authorize"

params = {
    "response_type": "code",
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "scope": "chat:write chat:read",
}

oauth_url = base_url + "?" + urllib.parse.urlencode(params)

print("===== KICK OAUTH LINK =====")
print(oauth_url)
print("===========================")
