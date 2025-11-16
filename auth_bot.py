from dotenv import load_dotenv
import os

# ŁADUJE .env Z KATALOGU REPOZYTORIUM
load_dotenv(dotenv_path=".env")

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
CLIENT_SECRET = os.getenv("KICK_CLIENT_SECRET")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")
CHANNELS = os.getenv("KICK_CHANNELS")

print("CLIENT_ID:", CLIENT_ID)
print("REDIRECT_URI:", REDIRECT_URI)

if not CLIENT_ID or not REDIRECT_URI:
    print("[AUTH ERROR] Brak CLIENT_ID lub REDIRECT_URI w .env!")
    exit(1)

print("[AUTH] Wygenerowałbym teraz link OAuth…")
