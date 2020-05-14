
import discord
from discord.ext import commands
import random
import math
import tictactoe as t 

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print('-----')

#Simple Test for Bot to respond back
@bot.command()
async def jing(ctx):
    await ctx.send('NO U')
#Simple Test for bot to add numbers
@bot.command()
async def add(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)
@bot.command()
async def tictactoe(ctx):
    await ctx.send("```" + t.main() + "```")


bot.run(TOKEN)

