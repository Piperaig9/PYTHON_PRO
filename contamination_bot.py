import discord
import random
import os 
from discord.ext import commands


lista = (os.listdir('images'))
lista2 = (os.listdir("contaminacion"))
reut = ("BOTELLA: al terminar de beber el liquido de una botella esta se puede llenar otra vez.",
        "BOLSAS: las bolsas que a uno le dan en los supermercados se pueden guardar y asi en un futuro guardar mas productos en esta.",
        "ROPA: la ropa vieja la puedes donar para no tener que desecharla."
        
        
        
        )

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def mem(ctx):
    lista_de_imagenes = os.listdir('images')
    image_aleatoria = random.choice(lista_de_imagenes)
    with open(f'images/{image_aleatoria}', 'rb') as f:
            picture = discord.File(f)



@bot.command()
async def con(ctx):
    lista_de_imagenes = os.listdir('contaminacion')
    image_aleatoria = random.choice(lista_de_imagenes)
    with open(f'contaminacion/{image_aleatoria}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def reutilizar(ctx):
     await ctx.send(random.choice(reut))


bot.run("TOKEN")
