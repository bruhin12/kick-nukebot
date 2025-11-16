import os
from dotenv import load_dotenv

# Wymuszamy ładowanie .env z katalogu głównego repo
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

# GENERUJEMY POPRAWNY LINK AUTH
url = (
    f"https://kick.com/oauth/authorize"
    f"?client_id={CLIENT_ID}"
    f"&redirect_uri={REDIRECT_URI}"
    f"&response_type=code"
    f"&scope=chat:write chat:read"
)

print("\n=== TWÓJ LINK OAUTH ===")
print(url)
print("\nWEJDŹ W TEN LINK JAKO BOT!")
