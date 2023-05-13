import discord
from Bard import Chatbot

with open("bis.txt", "r") as f:
    TOKEN = f.readline().strip()

with open("tris.txt", "r") as f:
    token = f.readline().strip()

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is online!")

@client.event
async def on_message(message):
    if message.content == "ping":
        await message.channel.send(f"Pong! {message.author.display_name}")

# Run the bot
client.run(TOKEN)