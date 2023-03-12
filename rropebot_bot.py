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
    
    # Bot is sending a first message
    start_work_em = discord.Embed(title="Time to start working!", color=0x7b165b)
    await ctx.send(embed = start_work_em)
    
    # Countdown will start after the following seconds
    await asyncio.sleep(3)
    
    # Bot is sending ending message
    start_break_em = discord.Embed(title="Time to rest!", color=0xc555ff)
    await ctx.send(embed = start_break_em) 

@bot.command(name="stop", help="Stop a Pomodoro timer")
async def stop_timer(ctx):
    
    # Bot is sending a first message
    stop_work_em = discord.Embed(title="Time to start working!", color=0x7b165b)
    await ctx.send(embed = stop_work_em)





#@client.event
# async def on_message(message):
    # if message.author == client.user: 
    #     return

    # if message.content.startswith('$hello'):
    #     await message.channel.send('Hello!')

bot.run(os.environ['BOT_TOKEN'])
