import discord
from Bard import Chatbot

with open("bis.txt", "r") as f:
    TOKEN = f.readline().strip()

with open("tris.txt", "r") as f:
    token = f.readline().strip()

client = discord.Client(intents=discord.Intents.all())

chatbot = Chatbot(token)

@client.event
async def on_ready():
    print("Bot is online!")

@client.event
async def on_message(message):
    resp=chatbot.ask(message)
    message.channel.reply(resp)

# Run the bot
client.run(TOKEN)