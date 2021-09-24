from pyrogram import Client

API_KEY = int(input("6951121"))
API_HASH = input("10654d2aa0d67e2f8759ba6a1644fa65")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
