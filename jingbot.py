
import discord
#import youtube_dl
from discord.ext import commands
import random
import math

TOKEN = 'NTAxNTU4ODkwNDgwMjcxMzYx.DqbSWw.mnLCt2tzPx453rBxDZzAy_hwXfI'

#client = discord.Client()
client = commands.Bot(command_prefix = '.')

players = {}


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if 'jing' in message.content:
        msg = '{0.author.mention} NO U'.format(message)
        await client.send_message(message.channel, msg)
        
    await client.process_commands(message)
    
@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context = True)
async def mth(ctx):
    equation = ""
    equation = ctx.message.content[4:]
    result = eval(equation)    
    await client.say(result)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
client.run(TOKEN)