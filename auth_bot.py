import os

client_id = os.getenv("KICK_CLIENT_ID")
redirect_uri = os.getenv("KICK_REDIRECT_URI")

if not client_id or not redirect_uri:
    print("[AUTH ERROR] Brak CLIENT_ID lub REDIRECT_URI w .env!")
    print("CLIENT_ID:", client_id)
    print("REDIRECT_URI:", redirect_uri)
    exit(1)

print(f"[AUTH] OAuth URL:")
print(f"https://kick.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=chat:write+user:read")
