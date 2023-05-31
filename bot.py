#1.4
import os
import discord
from discord.ext import commands
from datetime import datetime, timezone, timedelta
import chat
from dotenv import load_dotenv

path = 'info.txt'
f = open(path, 'r')
info=f.read()
f.close()
print(info)

load_dotenv()
discord_key=os.getenv("discord")

bot = commands.Bot(command_prefix='+',intents=discord.Intents.all())

level=0.8
token=4000

@bot.event
async def on_ready():
    print(f'{bot.user} is online!\nnow temperature is {level}')

@bot.command(name='thelp')
async def thelp(ctx):
    embed=discord.Embed(title="help list", color=0x1494f5,timestamp=datetime.now(timezone(timedelta(hours=+8))))
    embed.set_author(name="chatBot", icon_url="https://cdn.discordapp.com/app-icons/973145092980375552/da80b4dc5988b53c06461209dd2193c5.png")
    embed.add_field(name="+talk", value="和ChatGPT聊天", inline=False)
    embed.add_field(name="+image", value="ChatGPT產生一張描述的照片(很貴少用一點)", inline=False)
    embed.add_field(name="+set", value="設定機器人溫度0.0~1.0", inline=False)
    embed.add_field(name="+now", value="顯示目前機器人溫度，預設0.8", inline=False)
    embed.add_field(name="+thelp", value="顯示此列表", inline=False)
    embed.add_field(name="此機器人所有資料擷取自2022年以前", value="", inline=False)
    embed.add_field(name="請將問題問清楚，不然有可能被機器人補字", value="", inline=False)
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
    print(f'{ctx.author} have a chat require')
    message = ctx.message.content
    user_message = "" + message[6 : len(message)]
    await ctx.reply(f'{chat.chat_prompt(level,user_message,token)}\n:from ChatGPT')    

@bot.command(name='stalk')
async def stalk(ctx):
    print(f'{ctx.author} have a chat require')
    message = ctx.message.content
    user_message = "" + message[7 : len(message)]
    await ctx.author.send(f'{chat.chat_prompt(level,user_message,token)}\n:from ChatGPT')

@bot.command(name='image')
async def image(ctx):
    print(f'{ctx.author} have a image requier')
    message = ctx.message.content
    user_message = "" + message[7 : len(message)]
    await ctx.reply(chat.image_prompt(user_message))

@bot.event
async def on_message(msg):
    if msg.channel == bot.get_channel(988075823091286122):
        if msg.content.startswith('希望') and msg.author != bot.user:
            print(f'{msg.author} have a wish')
            await msg.channel.send(f'{chat.chat_prompt(0.5,msg.content,1000)}\n:from ChatGPT') 

bot.run(discord_key)