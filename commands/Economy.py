import random
from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands

from components import EcoEmbed
from functions import getplayer, playerload


class Economy(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        description="Ve cuántos peniques tienes o cuántos tiene algún miembro"
    )
    async def balance(
        self, interaction: discord.Interaction, miembro: Optional[discord.Member]
    ):
        await interaction.response.defer()

        pl = getplayer(interaction.user, miembro)
        em = EcoEmbed(self.bot, pl.id)

        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1138/1138038.png")

        em.add_field(name="👛 Bolsa", value=f"`{pl.pocket:^9,}`")
        em.add_field(name="🏦 Banco", value=f"`{pl.bank:^9,}`")
        em.add_field(name="🪙 V. Neto", value=f"`{pl.pocket + pl.bank:^9,}`")

        await interaction.followup.send(embed=em)

    @app_commands.checks.cooldown(2, 86400, key=lambda i: i.user.id)
    @app_commands.command(description="Gana peniques dos veces cada dia")
    async def ganar(self, interaction: discord.Interaction):
        await interaction.response.defer()

        id = interaction.user.id
        pl = playerload(id)
        earns = random.randint(1, random.randint(50, 200))
        em = EcoEmbed(self.bot, pl.id)

        pl.pocket += earns
        em.set_thumbnail(
            url="https://cdn-icons-png.flaticon.com/512/10749/10749511.png"
        )

        if bool(pl.save()):
            em.color = discord.Color.green()
            em.description = (
                f"Ganaste 🪙 `{earns}`\nAhora tienes 👛 `{pl.pocket:,}` en la bolsa"
            )
        else:
            em.color = discord.Color.dark_red()
            em.description = f"Tuve un 💨\nNo pude guardar \nGanancia de 🪙 `{earns}`"

        await interaction.followup.send(embed=em)


async def setup(bot):
    await bot.add_cog(Economy(bot))
