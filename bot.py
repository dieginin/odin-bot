import discord
from discord.ext import commands

from config import DISCORD_TOKEN
from connections import DBClient
from functions import cogload

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"BOT {bot.user} connected to Discord!")
    print(f"MDB connected: {DBClient().test()}")
    print(f"COG {await cogload(bot)} commands loaded")
    print("CMD sincronizando")
    print(f"CMD {len(await bot.tree.sync())} sincronizado")


bot.run(f"{DISCORD_TOKEN}")
