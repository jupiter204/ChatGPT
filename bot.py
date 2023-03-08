from discord.ext import commands
from chat import chat_prompt

bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

@bot.command(name='talk')
async def talk(ctx):
    print(f'{ctx.author} have a require')
    message = ctx.message.content
    user_message = "" + message[6 : len(message)]
    await ctx.reply(f'{chat_prompt(user_message)}   :from ChatGPT')
bot.run('OTczMTQ1MDkyOTgwMzc1NTUy.GeG4tf.0dZKUVRLTBixpBXqF47EL6dzMMmR7wf6VUQb6U')