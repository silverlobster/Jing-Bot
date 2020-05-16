
import discord
from discord.ext import commands
import random
import math
import tictactoe as t 

bot = commands.Bot(command_prefix = '.')

tic = t.TicTacToe()

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
#Command to display tictactoe board
@bot.command()
async def tictactoe(ctx):
    await ctx.send("```" + tic.display() + "```")
#Command to add symbol to tictactoe board
@bot.command()
async def add(ctx, coord: str):
    tic.add(coord)
    await ctx.send("```" + tic.display() + "```")


bot.run(TOKEN)

