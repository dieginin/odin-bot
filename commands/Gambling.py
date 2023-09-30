import random

import discord
from discord import app_commands
from discord.ext import commands

from components import EcoEmbed
from errors import InsufficientCoins, MinimunAmount
from functions import playerload


class Gambling(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.describe(cantidad="Ingresa los peniques que deseas apostar")
    @app_commands.command(
        description="Apuesta tus peniques con probabilidad de ganas o perder"
    )
    async def apostar(self, interaction: discord.Interaction, cantidad: int = 1000):
        if cantidad < 200:
            raise MinimunAmount(200)

        await interaction.response.defer()

        id = interaction.user.id
        pl = playerload(id)

        if pl.pocket < cantidad:
            raise InsufficientCoins(cantidad, pl.pocket)

        em = EcoEmbed(self.bot, pl.id)
        em.set_thumbnail(
            url="https://cdn-icons-png.flaticon.com/512/10749/10749451.png"
        )

        user_strikes = random.randint(1, 15)
        bot_strikes = random.randint(5, 15)

        if user_strikes > bot_strikes:
            percentage = random.randint(10, 100)
            amount = int(cantidad * (percentage / 100))
            pl.pocket += amount
            pl.save()

            em.color = discord.Color.green()
            em.description = f"Ganaste! 🪙 `{amount:,}`\nPorcentaje **{percentage}%**\nAhora tienes 👛 `{pl.pocket:,}`"
        elif user_strikes < bot_strikes:
            percentage = random.randint(0, 95)
            amount = int(cantidad * (percentage / 100))
            pl.pocket -= amount
            pl.save()

            em.color = discord.Color.red()
            em.description = f"Persiste! 🪙 `{amount:,}`\nPorcentaje **{percentage}%**\nAhora tienes 👛 `{pl.pocket:,}`"
        else:
            em.color = discord.Color.orange()
            em.description = f"Empate! 🪙 \nTu bolsa se queda en 👛 `{pl.pocket:,}`"

        await interaction.followup.send(embed=em)


async def setup(bot):
    await bot.add_cog(Gambling(bot))
