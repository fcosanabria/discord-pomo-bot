import asyncio
import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

# This example requires the 'message_content' intent.

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

#@client.event
@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))

@bot.command(name="start", help="Starts a Pomodoro timer")
async def start_timer(ctx):
    await ctx.send("Time to work!")
    await asyncio.sleep(10)
    await ctx.send("Time to play!")

#@client.event
# async def on_message(message):
    # if message.author == client.user:
    #     return

    # if message.content.startswith('$hello'):
    #     await message.channel.send('Hello!')

bot.run(os.environ['BOT_TOKEN'])
