from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands

from functions import getplayer


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
        m = discord.utils.get(self.bot.get_all_members(), id=pl.id)

        em = discord.Embed(color=discord.Color.random())
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1138/1138038.png")
        if m:
            em.set_author(name=m.display_name, icon_url=m.display_avatar.url)

        em.add_field(name="👛 Bolsa", value=f"`{pl.pocket:^9,}`")
        em.add_field(name="🏦 Banco", value=f"`{pl.bank:^9,}`")
        em.add_field(name="🪙 V. Neto", value=f"`{pl.pocket + pl.bank:^9,}`")

        await interaction.followup.send(embed=em)


async def setup(bot):
    await bot.add_cog(Economy(bot))
