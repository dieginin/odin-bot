import discord
from discord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, interaction: discord.Interaction, error):
        raise


async def setup(bot):
    cog = ErrorHandler(bot)
    bot.tree.on_error = cog.on_command_error
    await bot.add_cog(cog)
