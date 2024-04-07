import discord
from discord.ext import commands
from SCore import *

data = SoTACore._json_read("config.json")
bot = commands.Bot(command_prefix=data["prefix"],intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Ready")
    SoTACore._logs(f"\n{bot.user} Ready to work, time: {SoTACore._time()[0]}, date: time: {SoTACore._time()[1]}", "log")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

bot.run(data["token"])
