import random
from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands

from components import EcoEmbed
from errors import (
    InsufficientBalance,
    InsufficientCoins,
    InsufficientResources,
    SecureCoins,
)
from functions import getplayer, playerload
from models import Animal


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
    @app_commands.command(description="Gana peniques y herramientas dos veces cada dia")
    async def ganar(self, interaction: discord.Interaction):
        await interaction.response.defer()

        id = interaction.user.id
        pl = playerload(id)
        earns = random.randint(1, random.randint(50, random.randint(200, 1000)))
        tool = random.choice(list(pl.tools.keys()))
        tearns = random.randint(1, random.randint(2, 5))
        em = EcoEmbed(self.bot, pl.id)

        pl.pocket += earns
        pl.change_tools(tool, tearns)
        em.set_thumbnail(
            url="https://cdn-icons-png.flaticon.com/512/10749/10749511.png"
        )

        if bool(pl.save()):
            em.color = discord.Color.green()
            em.description = f"Ganaste 🪙 `{earns}`\nAhora tienes 👛 `{pl.pocket:,}`\nTambién ganaste `x{tearns}` :{tool}:"
        else:
            em.color = discord.Color.dark_red()
            em.description = f"Tuve un 💨\nNo pude guardar \nGanancia de 🪙 `{earns}`"

        await interaction.followup.send(embed=em)

    @app_commands.checks.cooldown(2, 86400, key=lambda i: i.user.id)
    @app_commands.command(
        description="Desposita peniques a tu cuenta de banco dos veces al dia"
    )
    async def depositar(self, interaction: discord.Interaction, cantidad: int):
        await interaction.response.defer()

        id = interaction.user.id
        pl = playerload(id)

        if pl.pocket < cantidad:
            raise InsufficientCoins(cantidad, pl.pocket)

        if pl.pocket - cantidad < 200:
            raise SecureCoins(cantidad, pl.pocket, 200)

        em = EcoEmbed(self.bot, pl.id)
        em.color = discord.Color.green()
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2580/2580315.png")

        pl.bank += cantidad
        pl.pocket -= cantidad
        pl.save()
        em.description = f"Depositaste 🪙 `{cantidad:,}`\n👛 `{pl.pocket:,}` en la bolsa\n🏦 `{pl.bank:,}` en el banco"

        await interaction.followup.send(embed=em)

    @app_commands.command(description="Retira peniques de tu cuenta de banco")
    async def retirar(self, interaction: discord.Interaction, cantidad: int):
        await interaction.response.defer()

        id = interaction.user.id
        pl = playerload(id)

        if pl.bank < cantidad:
            raise InsufficientBalance(cantidad, pl.bank)

        em = EcoEmbed(self.bot, pl.id)
        em.color = discord.Color.orange()
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4634/4634765.png")

        pl.bank -= cantidad
        pl.pocket += cantidad
        pl.save()
        em.description = f"Retiraste 🪙 `{cantidad:,}`\n👛 `{pl.pocket:,}` en la bolsa\n🏦 `{pl.bank:,}` en el banco"

        await interaction.followup.send(embed=em)

    @app_commands.command(description="Retira peniques de tu cuenta de banco")
    async def inventario(
        self, interaction: discord.Interaction, miembro: Optional[discord.Member]
    ):
        await interaction.response.defer()

        pl = getplayer(interaction.user, miembro)
        em = EcoEmbed(self.bot, pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1034/1034813.png")

        em.add_field(name="🏹 Arcos", value=f'`{pl.tools.get("bow_and_arrow"):^9,}`')
        em.add_field(
            name="🎣 Cañas", value=f'`{pl.tools.get("fishing_pole_and_fish"):^9,}`'
        )
        em.add_field(name="⛏️ Picos", value=f'`{pl.tools.get("pick"):^9,}`')

        animals_ = [
            f':{pl.animals[animal]["animal"]["hash"]}: {pl.animals[animal]["animal"]["name"]} `x{pl.animals[animal]["quantity"]}`'
            for animal in pl.animals
        ]
        fishes_ = [
            f':{pl.fishes[fish]["fish"]["hash"]}: {pl.fishes[fish]["fish"]["name"]} `x{pl.fishes[fish]["quantity"]}`'
            for fish in pl.fishes
        ]
        animals_ = "\n".join(animals_) if len(animals_) > 0 else "*Sin animales*"
        fishes_ = "\n".join(fishes_) if len(fishes_) > 0 else "*Sin peces*"

        em.add_field(name="**☵ Animales**", value=animals_)
        em.add_field(name="**☵ Peces**", value=fishes_)
        em.add_field(name="**☵ Reliquias**", value="*Sin reliquias*")

        await interaction.followup.send(embed=em)

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
    await bot.add_cog(Economy(bot))
