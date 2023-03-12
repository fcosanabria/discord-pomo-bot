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
    
    """await send()
    The await send(embed) comes from the following documentation: https://discordpy.readthedocs.io/en/stable/api.html?highlight=embed#discord.Webhook.send
    
     The await keyword is used to indicate that the code is asynchronous and that the program should wait for the operation to complete before moving on to the next task. ctx likely refers to the context in which the message is being sent, and send is the method being used to send the message.

    The embed parameter allows you to format the message in a more visually appealing way using an embed. stop_work_em is likely a variable that stores the content of the embed.
    """    


@bot.command(name="stop", help="Stop a Pomodoro timer")
async def stop_timer(ctx):
    
    # Bot is sending a first message
    stop_work_em = discord.Embed(title="Timer has been stopped!", color=0xff3c43)
    await ctx.send(embed = stop_work_em)





#@client.event
# async def on_message(message):
    # if message.author == client.user: 
    #     return

    # if message.content.startswith('$hello'):
    #     await message.channel.send('Hello!')

bot.run(os.environ['BOT_TOKEN'])
