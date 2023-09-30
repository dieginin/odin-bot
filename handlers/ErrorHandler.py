import discord
from discord import app_commands
from discord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def format_cooldown(seconds):
        days = seconds // 86400
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        formatted_cooldown = ""
        if days:
            formatted_cooldown += f"`{int(days)}` día(s), "
        if hours:
            formatted_cooldown += f"`{int(hours)}` hrs, "
        if minutes:
            formatted_cooldown += f"`{int(minutes)}` mins, "
        if seconds:
            formatted_cooldown += f"`{int(seconds)}` segs"

        return formatted_cooldown

    @commands.Cog.listener()
    async def on_command_error(self, interaction: discord.Interaction, error):
        if isinstance(error, app_commands.CommandOnCooldown):
            cd = self.format_cooldown(error.retry_after)
            em = discord.Embed(
                color=discord.Color.dark_red(),
                title="Cooldown",
                description=f"El comando esta durmiendo\nIntentalo de nuevo en:\n{cd}",
            )
            em.set_thumbnail(
                url="https://cdn-icons-png.flaticon.com/512/4116/4116112.png"
            )
            await interaction.response.send_message(
                embed=em, ephemeral=True, delete_after=10
            )
        else:
            raise


async def setup(bot):
    cog = ErrorHandler(bot)
    bot.tree.on_error = cog.on_command_error
    await bot.add_cog(cog)
