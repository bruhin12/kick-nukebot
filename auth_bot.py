import os
import urllib.parse

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")

def generate_oauth_link():
    if not CLIENT_ID or not REDIRECT_URI:
        print("[AUTH ERROR] Brak CLIENT_ID lub REDIRECT_URI w .env!")
        return

    base = "https://kick.com/oauth/authorize"
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "chat:read chat:write"
    }

    url = base + "?" + urllib.parse.urlencode(params)

    print("")
    print("==============================================")
    print(" 🔐 LINK DO AUTORYZACJI KICK OAUTH (WEJDŹ!)")
    print("==============================================")
    print(url)
    print("==============================================")
    print("")
    return url


if __name__ == "__main__":
    generate_oauth_link()
