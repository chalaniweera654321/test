from flask import Flask, request, jsonify
import asyncio
from discord import Client, Intents
import os

app = Flask(__name__)

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1497266855969161367

intents = Intents.default()
client = Client(intents=intents)

loop = asyncio.get_event_loop()

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

async def send_msg(content):
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(content)

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    msg = data.get("message")

    asyncio.run_coroutine_threadsafe(send_msg(msg), loop)

    return jsonify({"status": "sent"})

def run_flask():
    app.run(host="0.0.0.0", port=5000)

import threading
threading.Thread(target=run_flask).start()

client.run(TOKEN)
