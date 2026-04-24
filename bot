import discord

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # IMPORTANT: allows reading message text
intents.messages = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as: {client.user}")
    print("Bot is ready to receive data...\n")


@client.event
async def on_message(message):
    # Ignore bot's own messages
    if message.author == client.user:
        return

    print("========== NEW INCOMING DATA ==========")
    print(f"Author: {message.author}")
    print(f"User ID: {message.author.id}")
    print(f"Channel: {message.channel}")
    print(f"Channel ID: {message.channel.id}")
    print(f"Guild: {message.guild}")
    print(f"Content: {message.content}")
    print("======================================\n")

    # Optional: reply back for testing
    if message.content.startswith("!test"):
        await message.channel.send("✅ Bot received your message!")


client.run(TOKEN)
