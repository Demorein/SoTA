import discord
from discord.ext import commands
from SCore import *
import os

SYS_PREFIX = "------------"
SERV_PREFIX = "************"

data = SoTACore._json_read("config.json")
bot = commands.Bot(command_prefix=data["prefix"],intents=discord.Intents.all())

@bot.event
async def on_ready():
    os.system("cls")
    print("Ready")
    SoTACore._logs(f"\n{bot.user} Ready to work, time: {SoTACore._time()[0]}, date: time: {SoTACore._time()[1]} {SYS_PREFIX}")

@bot.command()
async def StartMS(ctx):
    embed = discord.Embed(
        title="Запуск сервера Minecraft!",
                                                    #FIXME Не пингуется пользователь 
        description=f"Запустил: @{ctx.author}\nВремя:{SoTACore._time()[0]}\nДата:{SoTACore._time()[1]}",
        color=0x008000,
    )
    embed.set_image(url=data["urlmine"])
    SoTACore._logs(log = f"\n\n@{ctx.author} запустил сервер Майнкрафт || Время:{SoTACore._time()[0]}Дата:{SoTACore._time()[1]} {SERV_PREFIX}\n")
    SoTACore.Minecraft._start(data["minedir"])
    await ctx.send(embed= embed)

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="SoTA",
        description="Проект, созданный для управления игровыми серверами через дискорд бота",
        color= 0xda4400
    )
    embed.set_image(url=data["urlSoTA"])
    await ctx.send(embed=embed)
    

bot.run(data["token"])
