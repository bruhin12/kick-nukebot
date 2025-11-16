import os
from dotenv import load_dotenv

# ---- WYMUSZONA LOKALIZACJA ENV ----
env_path = os.path.join(os.getcwd(), ".env")
print(f"[DEBUG] Loading .env from: {env_path}")

if not os.path.exists(env_path):
    print("[DEBUG ERROR] .env file DOES NOT EXIST!")
else:
    print("[DEBUG] .env file FOUND")

load_dotenv(env_path)

# ---- TEST ----
CLIENT_ID = os.getenv("KICK_CLIENT_ID")
CLIENT_SECRET = os.getenv("KICK_CLIENT_SECRET")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")
CHANNELS = os.getenv("KICK_CHANNELS")

print(f"[DEBUG] CLIENT_ID={CLIENT_ID}")
print(f"[DEBUG] REDIRECT_URI={REDIRECT_URI}")

# ---- WALIDACJA ----
if not CLIENT_ID or not REDIRECT_URI:
    print("[AUTH ERROR] Missing CLIENT_ID or REDIRECT_URI!")
    print("CLIENT_ID:", CLIENT_ID)
    print("REDIRECT_URI:", REDIRECT_URI)
    exit(1)

# --- GENEROWANIE LINKU ----
oauth_link = (
    f"https://kick.com/oauth/authorize"
    f"?client_id={CLIENT_ID}"
    f"&redirect_uri={REDIRECT_URI}"
    f"&response_type=code"
    f"&scope=chat:write chat:read"
)

print("\n[AUTH] OAuth Link:")
print(oauth_link)
print("\nWejdź tym linkiem jako BOT aby dokończyć autoryzację.")
