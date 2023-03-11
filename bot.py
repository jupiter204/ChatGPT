import os
import discord
from discord.ext import commands
from datetime import datetime, timezone, timedelta
from chat import chat_prompt
from dotenv import load_dotenv

load_dotenv()
discord_key=os.getenv("discord")

bot = commands.Bot(command_prefix='+',intents=discord.Intents.all())

level=0.8

@bot.event
async def on_ready():
    print(f'{bot.user} is online!\nnow temperature is {level}')

@bot.command(name='thelp')
async def thelp(ctx):
    embed=discord.Embed(title="help list", color=0x1494f5,timestamp=datetime.now(timezone(timedelta(hours=+8))))
    embed.set_author(name="chatBot", icon_url="https://cdn.discordapp.com/app-icons/973145092980375552/da80b4dc5988b53c06461209dd2193c5.png")
    embed.add_field(name="+talk", value="和ChatGPT聊天", inline=False)
    embed.add_field(name="+set", value="設定機器人溫度0.0~1.0", inline=False)
    embed.add_field(name="+now", value="顯示目前機器人溫度，預設0.8", inline=False)
    embed.add_field(name="+thelp", value="顯示此列表", inline=False)
    await ctx.reply(embed=embed)

@bot.command(name='now')
async def now(ctx):
    await ctx.reply(f'now temperature is {level}')

@bot.command(name='set')
async def set(ctx):
    message= ctx.message.content
    global level
    level = float("" + message[5 : len(message)])
    print(f'{ctx.author} set temperature to {level}')
    await ctx.reply(f'set temperature to {level}')

@bot.command(name='talk')
async def talk(ctx):
    print(f'{ctx.author} have a require')
    message = ctx.message.content
    user_message = "" + message[6 : len(message)]
    await ctx.reply(f'{chat_prompt(level,user_message)}\n:from ChatGPT')

bot.run(discord_key)