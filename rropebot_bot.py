import asyncio
import discord
import os
from dotenv import load_dotenv

# This example requires the 'message_content' intent.

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!')

#@client.event
@bot.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@bot.command(name:"start", help="Starts a Pomodoro timer")
async def start_timer(ctx):
    await

#@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.environ['BOT_TOKEN'])
