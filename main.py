import disnake
from disnake.ext import commands
from SCore import *
from dis import disco
import os
import tracemalloc

tracemalloc.start()

#PREFIXS
SYS_PREFIX = "------------"
SERV_PREFIX = "************"

#Objects
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True
data = SoTACore._json_read("config.json")
bot = commands.Bot(command_prefix=data["prefix"],intents=disnake.Intents.all(), test_guilds=[1226160999250526238])


#EVENT on_ready
@bot.event
async def on_ready():
    os.system("cls")
    print("Ready")
    SoTACore._logs(f"\n{bot.user} Ready to work, time: {SoTACore._time()[0]}, date: time: {SoTACore._time()[1]} {SYS_PREFIX}")
    

@bot.slash_command()
async def helps(ctx):
    embed = disnake.Embed(
        title="Help Command",
        description="/help - Выводит это сообщение\n/startserver [servername] - Запускает сервер\n/info - Информация о боте"
    )
    embed.set_thumbnail(url=data["urlhelp"])
    channel = bot.get_channel(1226160999250526241)
    await channel.send(embed=embed)


@bot.slash_command()
async def startserver(ctx, server:str):
    if SoTACore.Server._start(server) == True:
        embed = disnake.Embed(
            title="Запуск сервера!",
            description=f"Запустил: @{ctx.author}\nВремя: {SoTACore._time()[0]}\nДата: {SoTACore._time()[1]}",
            color=0x2ec700
        )
        embed.set_thumbnail(url=data["urlmine"])
        SoTACore._logs(f"Запустил: @{ctx.author} Время: {SoTACore._time()[0]} Дата: {SoTACore._time()[1]}")
        await ctx.send(embed=embed)
    else:
        embed = disnake.Embed(
            title="ERROR 404",
            description="ServerName is NotFound",
            color=0xed0000
        )
        embed.set_thumbnail(url=data["urlnotfound"])
        SoTACore._logs(f"Команда от: {ctx.author} NOT FOUND 404 Время: {SoTACore._time()[0]} Дата: {SoTACore._time()[1]}")
        await ctx.send(embed=embed)


# @bot.slash_command()
# async def stopserver(ctx, server:str):
#     if SoTACore.Server._close(server) == True:
#         embed = disnake.Embed(
#             title="Остановка сервера",
#             description=f"Остановил: @{ctx.author}\nВремя: {SoTACore._time()[0]}\nДата: {SoTACore._time()[1]}",
#             color=0xff9300
#         )
#         embed.set_thumbnail(url=data["urlmine"])
#         SoTACore._logs(f"Запустил: @{ctx.author} Время: {SoTACore._time()[0]} Дата: {SoTACore._time()[1]}")
#         await ctx.send(embed=embed)
#     else:
#         embed = disnake.Embed(
#             title="ERROR 404",
#             description="ServerName is NotFound",
#             color=0xed0000
#         )
#         embed.set_thumbnail(url=data["urlnotfound"])
#         SoTACore._logs(f"Команда от: {ctx.author} NOT FOUND 404 Время: {SoTACore._time()[0]} Дата: {SoTACore._time()[1]}")
#         await ctx.send(embed=embed)


@bot.slash_command()
async def info(ctx):
    embed = disnake.Embed(
        title="**SoTA**",
        description="Name:SoTA\nDescription:Проект, созданный для управления игровыми серверами через дискорд бота\nCore:SoTA Core\nCreator:Demorien\nVersion: 1.7-a",
        color= 0xda4400
    )
    
    embed.add_field(name="GitHub", value="https://github.com/Demorein/SoTA")
    embed.set_thumbnail(url=data["urlSoTA"])
    await ctx.send(embed=embed)

bot.run(data["token"])
