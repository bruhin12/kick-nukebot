import asyncio
import json
import sqlite3
import websockets
import aiohttp

# ============================================================
#  ŁADOWANIE TOKENÓW Z kick_tokens.db
# ============================================================

def load_tokens():
    conn = sqlite3.connect("kick_tokens.db")
    c = conn.cursor()
    c.execute("SELECT access_token, refresh_token FROM tokens LIMIT 1")
    row = c.fetchone()
    conn.close()

    if not row:
        print("[ERROR] Brak tokenów w kick_tokens.db!")
        return None, None

    access, refresh = row
    return access, refresh


ACCESS_TOKEN, REFRESH_TOKEN = load_tokens()

if not ACCESS_TOKEN:
    raise SystemExit("Brak access_token — zakończono.")


# ============================================================
#  KONFIGURACJA BOTA
# ============================================================

CHANNEL = "lodomirxpp"         # kanał bota
TARGET_MESSAGE = "!nuke"       # trigger
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}


# ============================================================
#  POBIERANIE CHATROOM ID ORAZ URL WEBSOCKET
# ============================================================

async def fetch_chatroom_info():
    url = f"https://kick.com/api/v2/channels/{CHANNEL}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            data = await r.json()
            try:
                chat_id = data["chatroom"]["id"]
                ws_url = data["chatroom"]["ws_url"]
                print("[BOT] Chatroom ID:", chat_id)
                print("[BOT] WebSocket URL:", ws_url)
                return chat_id, ws_url
            except:
                print("[ERROR] Kick API nie zwróciło chatroom!")
                print(data)
                raise


# ============================================================
#  WYSYŁANIE WIADOMOŚCI
# ============================================================

async def send_chat_message(ws, message):
    payload = {
        "event": "SendMessage",
        "data": {
            "content": message
        }
    }
    await ws.send(json.dumps(payload))


# ============================================================
#  FUNKCJA BANOWANIA
# ============================================================

async def ban_user(username):
    api_url = "https://kick.com/api/v2/moderation/ban"

    payload = {
        "channel": CHANNEL,
        "target": username,
        "reason": "Nuke bot auto-ban"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, headers=HEADERS, json=payload) as r:
            try:
                data = await r.json()
            except:
                data = {}
            print(f"[BAN] {username}: {data}")


# ============================================================
#  GŁÓWNA PĘTLA ODBIORU WIADOMOŚCI
# ============================================================

async def run_bot():
    chat_id, ws_url = await fetch_chatroom_info()

    async with websockets.connect(ws_url) as ws:
        print("[BOT] Połączono z WebSocket!")

        await send_chat_message(ws, "Bot aktywny i gotowy! ✨")

        while True:
            msg = await ws.recv()
            try:
                data = json.loads(msg)
            except:
                continue

            # filtrujemy tylko wiadomości
            if data.get("event") != "MessageSent":
                continue

            username = data["data"]["sender"]["username"]
            content = data["data"]["content"]

            print(f"[CHAT] {username}: {content}")

            # komenda nuke
            if content.lower().startswith("!nuke "):
                word = content.split(" ", 1)[1].strip().lower()
                global TARGET
                TARGET = word
                await send_chat_message(ws, f"Nuke aktywny — cel: '{word}'")

            # automatyczny ban
            try:
                if TARGET and TARGET in content.lower():
                    print(f"[NUKE] BAN: {username}")
                    await ban_user(username)
            except:
                pass


# ============================================================
#  START BOTA
# ============================================================

if __name__ == "__main__":
    TARGET = None

    print("[BOT] Start bota z tokenami kick_tokens.db")
    asyncio.run(run_bot())
