import sqlite3
import time
import requests
import json

DB_PATH = "kick_tokens.db"

API_CHAT_SEND = "https://kick.com/api/v2/messages/send"

# === Funkcja ładowania tokenów z bazy ===
def load_tokens():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT access_token, refresh_token, expires_at, scope FROM tokens LIMIT 1")
    row = c.fetchone()
    conn.close()

    if not row:
        raise Exception("❌ Brak tokenów w kick_tokens.db!")

    access_token, refresh_token, expires_at, scope = row

    print("=== TOKENY ZAŁADOWANE ===")
    print("access_token:", access_token[:20] + "...")
    print("refresh_token:", refresh_token[:20] + "...")
    print("expires_at:", expires_at)
    print("scope:", scope)

    return {
        "access": access_token,
        "refresh": refresh_token,
        "expires": expires_at,
        "scope": scope,
    }


# === Funkcja odświeżania tokena (jeśli masz CLIENT_SECRET) ===
def refresh_token(data):
    print("⚠ Refresh token przepuszczony — używamy stałych tokenów!")
    return data["access"]


# === Funkcja wysyłania wiadomości do czatu ===
def send_message(channel_id, msg, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "channel_id": int(channel_id),
        "content": msg
    }

    r = requests.post(API_CHAT_SEND, json=payload, headers=headers)

    print(">> Chat response:", r.status_code, r.text)
    return r.status_code == 200


# === GŁÓWNY BOT ===
def main():
    print("[BOT] Start GitHub bot")

    try:
        tokens = load_tokens()
    except Exception as e:
        print("Error:", e)
        exit(1)

    token = tokens["access"]

    CHANNEL_ID = YOUR_CHANNEL_ID_HERE   # <<< WPISZ ID KANAŁU

    print("[BOT] Bot działający. Piszę co 10 sek...")

    while True:
        send_message(CHANNEL_ID, "Bot działa ✔", token)
        time.sleep(10)


if __name__ == "__main__":
    main()
