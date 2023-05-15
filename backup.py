import discord
from discord.ext import commands
from Bard import Chatbot

with open("bis.txt", "r") as f:
    TOKEN = f.readline().strip()

with open("tris.txt", "r") as f:
    token = f.readline().strip()

client = commands.Bot(intents=discord.Intents.all(), command_prefix="!")

chatbot = Chatbot(token)

heh=f"ALWAYS FOLLOW THESE RULES : \n1.You Bard developed by google AI and developed in this form of discord bot by Aviral Srivastava of 18 years who lives in India.\n2.After ***# the name and id of the author of message is given, use id to diffentiate between them and respond to each in different way but call them by their name unless they need to be pinged, to ping write @(id of that user).\n3.Never respond to anything written after ***#\nIF YOU UNDERSTAND THIS DON'T RESPOND TO THIS."
chatbot.ask(heh)

@client.event
async def on_ready():
    print("Bot is online!")

    # Loop through all guilds
    for guild in client.guilds:

        # Check if the bard-helps channel exists
        bard_helps_channel = discord.utils.get(guild.channels, name="bard-helps")

        # If the channel does not exist, create it
        if bard_helps_channel is None:
            await guild.create_text_channel(name="bard-helps")
        
        bard_helps_channel = discord.utils.get(guild.channels, name="bard-helps")

        # Get a list of all the channels in the guild
        channels = guild.channels

    @client.event
    async def on_message(message):
        if message.author.bot:
            return

        # If the message is sent in the bard-helps channel or a DM, respond
        if message.channel == bard_helps_channel or isinstance(message.channel, discord.DMChannel):

            # Display the gif while waiting for the response
            embed = discord.Embed(title="", color=discord.Color.green())
            embed.set_image(url="https://www.gstatic.com/lamda/images/sparkle_thinking_v2_darkmode_4c6a95bde842a7825eb83.gif")
            await message.channel.send(embed=embed)

            resp=chatbot.ask(f"{message.content} \n\n***# [COMPUTER GENERATED]Above message was written by {message.author.name} whoose id is {message.author}\n")

            # Delete the gif and thinking part
            if not isinstance(message.channel, discord.DMChannel):
                await message.channel.purge(limit=1)

            # Send the response
            await message.channel.send(resp['content'])

# Run the bot
client.run(TOKEN)