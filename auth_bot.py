from dotenv import load_dotenv
import os

env_path = os.path.join(os.getcwd(), ".env")
print(f"[DEBUG] Loading .env from: {env_path}")
load_dotenv(env_path)

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")

print(f"CLIENT_ID: {CLIENT_ID}")
print(f"REDIRECT_URI: {REDIRECT_URI}")

def generate_oauth():
    if not CLIENT_ID or not REDIRECT_URI:
        print("[AUTH ERROR] Brak CLIENT_ID lub REDIRECT_URI w .env!")
        return
    
    link = (
        "https://id.kick.com/oauth/authorize?"
        f"response_type=code&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=user:read+chat:read+chat:write+moderation:write+events:subscribe"
    )

    print("=== TWÓJ LINK OAUTH ===")
    print(link)
    print("WEJDŹ W TEN LINK JAKO BOT!")

if __name__ == "__main__":
    generate_oauth()

