import discord
from discord.ext import commands

from connections import DBClient


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        id = message.author.id
        client = DBClient()

        if not client.find(id):
            client.insert(id, {"pocket": 100, "bank": 0})


async def setup(bot):
    await bot.add_cog(Event(bot))
