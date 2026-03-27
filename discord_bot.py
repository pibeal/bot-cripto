import discord
import os
from discord.ext import commands

# Configuramos los permisos (Intents)
intents = discord.Intents.default()
intents.message_content = True  # Permite leer el contenido de los mensajes

# Definimos el prefijo de los comandos (ejemplo: !hola)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'¡Bot encendido como {bot.user}!')

@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! Soy tu bot de Discord configurado desde GitHub.')

# Esta línea busca la variable que configuraremos en Railway
token = os.getenv('DISCORD_TOKEN')
bot.run(token)

