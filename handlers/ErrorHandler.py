import discord
from discord import app_commands
from discord.ext import commands

from errors import *


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
        elif isinstance(error.__cause__, MinimunAmount):
            coins = error.__cause__.coins
            em = discord.Embed(
                color=discord.Color.dark_red(),
                title="Cantidad Mínima",
                description=f"Cantidad bajo el mínimo\nIngresa 🪙 `{coins:^5,}` o más",
            )
            em.set_thumbnail(
                url="https://cdn-icons-png.flaticon.com/512/461/461046.png"
            )
            await interaction.response.send_message(
                embed=em, ephemeral=True, delete_after=10
            )
        elif isinstance(error.__cause__, InsufficientCoins):
            coins, pocket = error.__cause__.coins, error.__cause__.pocket

            em = discord.Embed(color=discord.Color.dark_red())
            em.title = "Monedas Insuficientes"
            em.description = f"No tienes 🪙 `{coins:,}`\nTienes 👛 `Bolsa: {pocket:,}`"
            em.set_thumbnail(
                url="https://cdn-icons-png.flaticon.com/512/4952/4952656.png"
            )

            await interaction.followup.send(embed=em)
        elif isinstance(error.__cause__, SecureCoins):
            coins, pocket, secure = (
                error.__cause__.coins,
                error.__cause__.pocket,
                error.__cause__.secure,
            )

            em = discord.Embed(color=discord.Color.dark_red())
            em.title = "Valla de Seguridad"
            em.description = f"**Siempre** debes de tener al menos **{secure}** contigo.\nIngresaste 🪙 `{coins:,}` y tienes 👛 `{pocket:,}`"
            em.set_thumbnail(
                url="https://cdn-icons-png.flaticon.com/512/6003/6003742.png"
            )

            await interaction.followup.send(embed=em)
        else:
            raise


async def setup(bot):
    cog = ErrorHandler(bot)
    bot.tree.on_error = cog.on_command_error
    await bot.add_cog(cog)
