import random

import discord
from discord import app_commands
from discord.ext import commands

from components import EcoEmbed
from errors import InsufficientResources
from functions import playerload
from models import Animal


class Activity(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description="Utiliza tus arcos para cazar animales")
    async def cazar(self, interaction: discord.Interaction):
        await interaction.response.defer()

        id = interaction.user.id
        pl = playerload(id)

        if pl.tools["bow_and_arrow"] <= 0:
            raise InsufficientResources("bow_and_arrow")

        em = EcoEmbed(self.bot, pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3553/3553171.png")

        pl.change_tools("bow_and_arrow", -1)
        weights = [a().probability for a in Animal.__subclasses__()]  # type: ignore
        animal = random.choices(Animal.__subclasses__(), weights=weights)[0]()  # type: ignore

        caza = random.choices([0, 1], weights=[0.1, 0.9], k=1)[0]
        if caza:
            pl.change_animal(animal, 1)
            em.color = discord.Color.green()
            em.description = f"**Felicidades!**\nCazaste un :{animal.hash}: `{animal.name}`\nTienes `x{pl.animals[animal.hash]['quantity']:,} {animal.name}`"
        else:
            em.color = discord.Color.red()
            em.description = f"**Oh no!**\nUn :{animal.hash}: `{animal.name}` se te escapó\nMejor suerte para la próxima"
        pl.save()

        await interaction.followup.send(embed=em)


async def setup(bot):
    await bot.add_cog(Activity(bot))
