import asyncio
import json
import os
import aiohttp
import websockets
from curl_cffi import requests

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
CLIENT_SECRET = os.getenv("KICK_CLIENT_SECRET")
REDIRECT_URI = os.getenv("KICK_REDIRECT_URI")
CHANNELS = [c.strip() for c in os.getenv("KICK_CHANNELS", "").split(",") if c.strip()]

TOKEN_DB = "tokens.json"


# ---------- TOKEN HANDLING ----------
def load_tokens():
    if not os.path.exists(TOKEN_DB):
        return {}
    with open(TOKEN_DB, "r") as f:
        return json.load(f)


def save_tokens(tokens):
    with open(TOKEN_DB, "w") as f:
        json.dump(tokens, f)


async def oauth_exchange(code: str):
    url = "https://id.kick.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }
    r = requests.post(url, data=data)
    tokens = r.json()
    save_tokens(tokens)
    return tokens


def get_valid_token():
    tokens = load_tokens()
    if "access_token" not in tokens:
        return None
    return tokens["access_token"]


# ---------- FETCH CHATROOM ----------
async def get_chatroom(username):
    url = f"https://kick.com/api/v2/channels/{username}"

    r = requests.get(url)
    if "chatroom" not in r.json():
        print("[ERROR] Kick API odmówiło dostępu! Chatroom blokowany.")
        print(r.json())
        return None, None

    info = r.json()
    chat_id = info["chatroom"]["id"]
    ws_url = info["chatroom"]["websocket_url"]
    return chat_id, ws_url


# ---------- MAIN BOT LOOP ----------
async def handle_chat(username):
    print(f"[BOT] Pobieram chatroom: {username}")

    chat_id, ws_url = await get_chatroom(username)
    if not chat_id:
        print("[BOT] Nie udało się pobrać chatroomu.")
        return

    print(f"[BOT] łączę WebSocket → {ws_url}")

    async with websockets.connect(ws_url) as ws:
        print(f"[BOT] Połączono z chatem: {username}")

        while True:
            try:
                message = await ws.recv()
                data = json.loads(message)

                # Kick wysyła różne eventy
                if "data" not in data:
                    continue

                msg = data["data"]

                # tylko chat messages
                if msg.get("type") != "message":
                    continue

                text = msg["content"].lower()
                user = msg["sender"]["username"]

                print(f"[CHAT] {user}: {text}")

                # NUKE
                if text.startswith("!nuke "):
                    target_text = text.replace("!nuke ", "").strip()
                    print(f"[NUKE] Szukam: {target_text}")

                    # Tu logika nukowania — placeholder
                    print("[NUKE] (github: wykonuję nuke — placeholder)")

            except Exception as e:
                print("WebSocket error:", e)
                await asyncio.sleep(5)


async def main():
    print("[BOT] Start GitHub bot")

    token = get_valid_token()
    if not token:
        print("[AUTH] Potrzebna autoryzacja Kick OAuth!")
        print("Wygeneruj link w logach GitHub Actions i wejdź nim jako BOT.")
        return

    tasks = [asyncio.create_task(handle_chat(ch)) for ch in CHANNELS]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
