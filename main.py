import discord
from discord.ext import commands
from config import token

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='=', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel("556280232643002372")
    await channel.send("¡Bienvenid@ al server! Saluden no sean groser@s ;D")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel("556280232643002372")
    await channel.send("Miau, se nos fue, nunca le dije que la amaba :( xd")
    
@bot.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel =ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("No estás en el canal de voz, para activar este comando debes de estar dentro de el.")

@bot.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Dejé el chat de voz.")
    else:
        await ctx.send("No estoy en el chat de voz.")

@bot.command(name='hola')
async def hola(ctx):
    await ctx.send('Miau, hola!')

@bot.command(name='adios')
async def hola(ctx):
    await ctx.send('Adios prro XD')

@bot.command(name='elosas')
async def hola(ctx):
    await ctx.send('elkamen xd')

@bot.command(name='mailyrul')
async def hola(ctx):
    await ctx.send('papas xd')
    
@bot.command(name='waza')
async def hola(ctx):
    await ctx.send('WAZAAAAAAAAAAA')

bot.run(token)

