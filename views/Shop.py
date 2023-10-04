import discord
from discord.ext import commands

from components import EcoEmbed
from models import Animal, Fish, Player, Relic


class ShopHome(discord.ui.View):
    def __init__(self, pl: Player, bot: commands.Bot):
        self.pl = pl
        self.bot = bot
        self.message: discord.Interaction
        super().__init__(timeout=90)

    @discord.ui.button(label="Comprar", style=discord.ButtonStyle.grey)
    async def buy(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3553/3553184.png")
        em.description = (
            "🏹 `x1` 500 peniques\n🎣 `x1` 500 peniques\n ⛏️ `x1` 500 peniques"
        )
        await interaction.response.edit_message(
            embed=em, view=ShopComprar(self.pl, self.bot)
        )

    @discord.ui.button(label="Vender", style=discord.ButtonStyle.grey)
    async def sell(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2372/2372853.png")
        if (
            len(self.pl.animals) > 0
            or len(self.pl.fishes) > 0
            or len(self.pl.relics) > 0
        ):
            em.description = "🏔️ `Animales`\n🌊 `Peces`\n📦 `Reliquias`"
            await interaction.response.edit_message(
                embed=em, view=ShopVender(self.pl, self.bot)
            )
        else:
            em.color = discord.Color.red()
            em.description = "Nada que vender\nPuedes hacer actividades\n`/cazar` `/pescar` `/encontrar`"
            await interaction.response.edit_message(
                embed=em, view=NoSell(self.pl, self.bot)
            )

    @discord.ui.button(label="Salir", style=discord.ButtonStyle.red)
    async def close(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1234/1234190.png")
        em.description = "**Gracias!**\nNos vemos pronto\n*Abierto 24/7*"
        await interaction.response.edit_message(embed=em, view=None)

    async def on_timeout(self):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1234/1234190.png")
        em.description = "**Gracias!**\nNos vemos pronto\n*Abierto 24/7*"
        try:
            await self.message.edit(embed=em, view=None)  # type: ignore
        except:
            pass
        self.stop()


class ShopComprar(discord.ui.View):
    def __init__(self, pl: Player, bot: commands.Bot):
        self.pl = pl
        self.bot = bot
        super().__init__()

    @discord.ui.button(emoji="🏹", style=discord.ButtonStyle.grey)
    async def bows(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3553/3553184.png")
        em.description = (
            "🏹 `x1` 500 peniques\n🏹 `x3` 1,500 peniques\n🏹 `x5` 2,500 peniques"
        )

        await interaction.response.edit_message(
            embed=em, view=ShopQty(self.pl, self.bot, "bow_and_arrow")
        )

    @discord.ui.button(emoji="🎣", style=discord.ButtonStyle.grey)
    async def rods(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3553/3553184.png")
        em.description = (
            "🎣 `x1` 500 peniques\n🎣 `x3` 1,500 peniques\n🎣 `x5` 2,500 peniques"
        )

        await interaction.response.edit_message(
            embed=em, view=ShopQty(self.pl, self.bot, "fishing_pole_and_fish")
        )

    @discord.ui.button(emoji="⛏️", style=discord.ButtonStyle.grey)
    async def picks(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3553/3553184.png")
        em.description = (
            "⛏️ `x1` 500 peniques\n ⛏️ `x3` 1,500 peniques\n ⛏️ `x5` 2,500 peniques"
        )

        await interaction.response.edit_message(
            embed=em, view=ShopQty(self.pl, self.bot, "pick")
        )

    @discord.ui.button(label="Regresar", style=discord.ButtonStyle.blurple, row=2)
    async def back(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4634/4634649.png")

        em.description = "**Tienda**\nHola bienvenido,\nQue deseas hacer?"
        await interaction.response.edit_message(
            embed=em, view=ShopHome(self.pl, self.bot)
        )

    @discord.ui.button(label="Salir", style=discord.ButtonStyle.red, row=2)
    async def close(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/1234/1234190.png")
        em.description = "**Gracias!**\nNos vemos pronto\n*Abierto 24/7*"
        await interaction.response.edit_message(embed=em, view=None)


class ShopVender(discord.ui.View):
    def __init__(self, pl: Player, bot: commands.Bot):
        self.pl = pl
        self.bot = bot
        super().__init__()

        if len(self.pl.animals) > 0:
            self.animals.disabled = False
        if len(self.pl.fishes) > 0:
            self.fishes.disabled = False
        if len(self.pl.relics) > 0:
            self.relics.disabled = False

    @discord.ui.button(emoji="🏔️", style=discord.ButtonStyle.grey, disabled=True)
    async def animals(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2372/2372853.png")
        em.description = f"\
:chicken: Pollo `10` peniques\n\
:hamster: Hamster `30` peniques\n\
:dog: Perro `40` peniques\n\
:cat: Gato `60` peniques\n\
:bird: Pájaro `80` peniques\n\
:rabbit: Conejo `100` peniques\n\
:monkey: Mono `150` peniques\n\
:fox: Zorro `200` peniques\n\
:wolf: Lobo `300` peniques\n\
:horse: Caballo `400` peniques\n\
:bear: Oso `500` peniques\n\
:elephant: Elefante `800` peniques\n\
:tiger: Tigre `1,000` peniques\n\
:lion: León `1,200` peniques\n\
:alien: Alien `1,500` peniques"

        await interaction.response.edit_message(
            embed=em, view=Sell(self.pl, self.bot, "animal")
        )

    @discord.ui.button(emoji="🌊", style=discord.ButtonStyle.grey, disabled=True)
    async def fishes(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2372/2372853.png")
        em.description = f"\
:shell: Concha `10` peniques\n\
:shrimp: Camarón `30` peniques\n\
:fish: Charal `40` peniques\n\
:crab: Cangrejo `60` peniques\n\
:blowfish: Fogu `80` peniques\n\
:lobster: Langosta `100` peniques\n\
:turtle: Tortuga `150` peniques\n\
:otter: Nutria `200` peniques\n\
:seal: Foca `300` peniques\n\
:octopus: Pulpo `400` peniques\n\
:dolphin: Delfín `500` peniques\n\
:squid: Calamar `800` peniques\n\
:shark: Tiburón `1,000` peniques\n\
:whale: Ballena `1,200` peniques\n\
:sauropod: Nessie `1,500` peniques"

        await interaction.response.edit_message(
            embed=em, view=Sell(self.pl, self.bot, "fish")
        )

    @discord.ui.button(emoji="📦", style=discord.ButtonStyle.grey, disabled=True)
    async def relics(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2372/2372853.png")
        em.description = f"\
:syringe: Jeringa `10` peniques\n\
:game_die: Dado `30` peniques\n\
:soccer: Balón `40` peniques\n\
:dart: Dardos `60` peniques\n\
:magic_wand: Varita `80` peniques\n\
:bell: Campana `100` peniques\n\
:lacrosse: Lacrosse `150` peniques\n\
:clock: Reloj `200` peniques\n\
:violin: Violín `300` peniques\n\
:trophy: Trofeo `400` peniques\n\
:rock: Piedra `500` peniques\n\
:bricks: Granito `800` peniques\n\
:diamond_shape_with_a_dot_inside: Turquesa `1,000` peniques\n\
:gem: Diamante `1,200` peniques\n\
:comet: Cometa `1,500` peniques"

        await interaction.response.edit_message(
            embed=em, view=Sell(self.pl, self.bot, "relic")
        )

    @discord.ui.button(label="Regresar", style=discord.ButtonStyle.blurple, row=2)
    async def back(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4634/4634649.png")

        em.description = "**Tienda**\nHola bienvenido,\nQue deseas hacer?"
        await interaction.response.edit_message(
            embed=em, view=ShopHome(self.pl, self.bot)
        )

    @discord.ui.button(label="Salir", style=discord.ButtonStyle.red, row=2)
    async def close(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/1234/1234190.png")
        em.description = "**Gracias!**\nNos vemos pronto\n*Abierto 24/7*"
        await interaction.response.edit_message(embed=em, view=None)


class ShopQty(discord.ui.View):
    def __init__(self, pl: Player, bot: commands.Bot, tool):
        self.pl = pl
        self.bot = bot
        self.tool = tool

        self.message: discord.Interaction
        super().__init__()

    @discord.ui.button(label="x1", style=discord.ButtonStyle.grey)
    async def one(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3553/3553184.png")
        btool = 1
        cost = 500 * btool
        if self.pl.pocket < cost:
            em.color = discord.Color.red()
            em.description = (
                f"Necesitas 🪙 `{cost:,}`\nTienes 👛 `{self.pl.pocket:,}`\nVuelve después"
            )
            return await interaction.response.edit_message(
                embed=em, view=ShopAgain(self.pl, self.bot, "buy", self.tool)
            )

        self.pl.change_tools(self.tool, btool)
        self.pl.pocket -= cost
        self.pl.save()

        em.color = discord.Color.green()
        em.description = f"**Compra exitosa!**\n:{self.tool}: `x{btool}` por 🪙 `{cost:,}`\n*Quieres hacer algo más?*"

        await interaction.response.edit_message(
            embed=em, view=ShopAgain(self.pl, self.bot, "buy", self.tool)
        )

    @discord.ui.button(label="x3", style=discord.ButtonStyle.grey)
    async def three(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3553/3553184.png")
        btool = 3
        cost = 500 * btool
        if self.pl.pocket < cost:
            em.color = discord.Color.red()
            em.description = (
                f"Necesitas 🪙 `{cost:,}`\nTienes 👛 `{self.pl.pocket:,}`\nVuelve después"
            )
            return await interaction.response.edit_message(
                embed=em, view=ShopAgain(self.pl, self.bot, "buy", self.tool)
            )

        self.pl.change_tools(self.tool, btool)
        self.pl.pocket -= cost
        self.pl.save()

        em.color = discord.Color.green()
        em.description = f"**Compra exitosa!**\n:{self.tool}: `x{btool}` por 🪙 `{cost:,}`\n*Quieres hacer algo más?*"

        await interaction.response.edit_message(
            embed=em, view=ShopAgain(self.pl, self.bot, "buy", self.tool)
        )

    @discord.ui.button(label="x5", style=discord.ButtonStyle.grey)
    async def five(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3553/3553184.png")
        btool = 5
        cost = 500 * btool
        if self.pl.pocket < cost:
            em.color = discord.Color.red()
            em.description = (
                f"Necesitas 🪙 `{cost:,}`\nTienes 👛 `{self.pl.pocket:,}`\nVuelve después"
            )
            return await interaction.response.edit_message(
                embed=em, view=ShopAgain(self.pl, self.bot, "buy", self.tool)
            )

        self.pl.change_tools(self.tool, btool)
        self.pl.pocket -= cost
        self.pl.save()

        em.color = discord.Color.green()
        em.description = f"**Compra exitosa!**\n:{self.tool}: `x{btool}` por 🪙 `{cost:,}`\n*Quieres hacer algo más?*"

        await interaction.response.edit_message(
            embed=em, view=ShopAgain(self.pl, self.bot, "buy", self.tool)
        )

    @discord.ui.button(label="Regresar", style=discord.ButtonStyle.blurple, row=2)
    async def back(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3553/3553184.png")
        em.description = (
            "🏹 `x1` 500 peniques\n🎣 `x1` 500 peniques\n ⛏️ `x1` 500 peniques"
        )
        await interaction.response.edit_message(
            embed=em, view=ShopComprar(self.pl, self.bot)
        )

    @discord.ui.button(label="Salir", style=discord.ButtonStyle.red, row=2)
    async def close(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/1234/1234190.png")
        em.description = "**Gracias!**\nNos vemos pronto\n*Abierto 24/7*"
        await interaction.response.edit_message(embed=em, view=None)


class ShopAgain(discord.ui.View):
    def __init__(self, pl: Player, bot: commands.Bot, mode: str, what: str):
        self.pl = pl
        self.bot = bot
        self.mode = mode
        self.what = what

        self.foco = (
            self.pl.animals
            if what == "animal"
            else self.pl.fishes
            if what == "fish"
            else self.pl.relics
        )

        self.message: discord.Interaction
        super().__init__()

    @discord.ui.button(label="Inicio", style=discord.ButtonStyle.grey)
    async def home(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4634/4634649.png")

        em.description = "**Tienda**\nHola bienvenido,\nQue deseas hacer?"
        await interaction.response.edit_message(
            embed=em, view=ShopHome(self.pl, self.bot)
        )

    @discord.ui.button(label="Atras", style=discord.ButtonStyle.blurple)
    async def back(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)

        if self.mode == "buy":
            em.set_thumbnail(
                url="https://cdn-icons-png.flaticon.com/512/3553/3553184.png"
            )
            # TODO regresar a buy
            em.description = (
                "🏹 `x1` 500 peniques\n🎣 `x1` 500 peniques\n ⛏️ `x1` 500 peniques"
            )
            await interaction.response.edit_message(
                embed=em, view=ShopComprar(self.pl, self.bot)
            )
        else:
            em.set_thumbnail(
                url="https://cdn-icons-png.flaticon.com/512/2372/2372853.png"
            )
            if len(self.foco) != 0:
                if self.what == "animal":
                    em.description = f"\
    :chicken: Pollo `10` peniques\n\
    :hamster: Hamster `30` peniques\n\
    :dog: Perro `40` peniques\n\
    :cat: Gato `60` peniques\n\
    :bird: Pájaro `80` peniques\n\
    :rabbit: Conejo `100` peniques\n\
    :monkey: Mono `150` peniques\n\
    :fox: Zorro `200` peniques\n\
    :wolf: Lobo `300` peniques\n\
    :horse: Caballo `400` peniques\n\
    :bear: Oso `500` peniques\n\
    :elephant: Elefante `800` peniques\n\
    :tiger: Tigre `1,000` peniques\n\
    :lion: León `1,200` peniques\n\
    :alien: Alien `1,500` peniques"
                elif self.what == "fish":
                    em.description = f"\
    :shell: Concha `10` peniques\n\
    :shrimp: Camarón `30` peniques\n\
    :fish: Charal `40` peniques\n\
    :crab: Cangrejo `60` peniques\n\
    :blowfish: Fogu `80` peniques\n\
    :lobster: Langosta `100` peniques\n\
    :turtle: Tortuga `150` peniques\n\
    :otter: Nutria `200` peniques\n\
    :seal: Foca `300` peniques\n\
    :octopus: Pulpo `400` peniques\n\
    :dolphin: Delfín `500` peniques\n\
    :squid: Calamar `800` peniques\n\
    :shark: Tiburón `1,000` peniques\n\
    :whale: Ballena `1,200` peniques\n\
    :sauropod: Nessie `1,500` peniques"
                else:
                    em.description = f"\
    :syringe: Jeringa `10` peniques\n\
    :game_die: Dado `30` peniques\n\
    :soccer: Balón `40` peniques\n\
    :dart: Dardos `60` peniques\n\
    :magic_wand: Varita `80` peniques\n\
    :bell: Campana `100` peniques\n\
    :lacrosse: Lacrosse `150` peniques\n\
    :clock: Reloj `200` peniques\n\
    :violin: Violín `300` peniques\n\
    :trophy: Trofeo `400` peniques\n\
    :rock: Piedra `500` peniques\n\
    :bricks: Granito `800` peniques\n\
    :diamond_shape_with_a_dot_inside: Turquesa `1,000` peniques\n\
    :gem: Diamante `1,200` peniques\n\
    :comet: Cometa `1,500` peniques"

                await interaction.response.edit_message(
                    embed=em, view=Sell(self.pl, self.bot, self.what)
                )
            else:
                if (
                    len(self.pl.animals) > 0
                    or len(self.pl.fishes) > 0
                    or len(self.pl.relics) > 0
                ):
                    em.description = "🏔️ `Animales`\n🌊 `Peces`\n📦 `Reliquias`"
                    await interaction.response.edit_message(
                        embed=em, view=ShopVender(self.pl, self.bot)
                    )
                else:
                    em.color = discord.Color.red()
                    em.description = "Nada que vender\nPuedes hacer actividades\n`/cazar` `/pescar` `/encontrar`"
                    await interaction.response.edit_message(
                        embed=em, view=NoSell(self.pl, self.bot)
                    )

    @discord.ui.button(label="Salir", style=discord.ButtonStyle.red)
    async def close(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/1234/1234190.png")
        em.description = "**Gracias!**\nNos vemos pronto\n*Abierto 24/7*"
        await interaction.response.edit_message(embed=em, view=None)


class NoSell(discord.ui.View):
    def __init__(self, pl: Player, bot: commands.Bot):
        self.pl = pl
        self.bot = bot
        self.message: discord.Interaction
        super().__init__()

    @discord.ui.button(label="Inicio", style=discord.ButtonStyle.grey)
    async def home(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4634/4634649.png")

        em.description = "**Tienda**\nHola bienvenido,\nQue deseas hacer?"
        await interaction.response.edit_message(
            embed=em, view=ShopHome(self.pl, self.bot)
        )

    @discord.ui.button(label="Salir", style=discord.ButtonStyle.red)
    async def close(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/1234/1234190.png")
        em.description = "**Gracias!**\nNos vemos pronto\n*Abierto 24/7*"
        await interaction.response.edit_message(embed=em, view=None)


class Sell(discord.ui.View):
    def __init__(self, pl: Player, bot: commands.Bot, what: str):
        self.pl = pl
        self.bot = bot

        self.message: discord.Interaction
        super().__init__()
        self.add_item(SellDropdown(pl, bot, what))

    @discord.ui.button(label="Inicio", style=discord.ButtonStyle.grey)
    async def home(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4634/4634649.png")

        em.description = "**Tienda**\nHola bienvenido,\nQue deseas hacer?"
        await interaction.response.edit_message(
            embed=em, view=ShopHome(self.pl, self.bot)
        )

    @discord.ui.button(label="Atras", style=discord.ButtonStyle.blurple)
    async def back(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2372/2372853.png")
        em.description = "🏔️ `Animales`\n🌊 `Peces`\n📦 `Reliquias`"
        await interaction.response.edit_message(
            embed=em, view=ShopVender(self.pl, self.bot)
        )

    @discord.ui.button(label="Salir", style=discord.ButtonStyle.red)
    async def close(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/1234/1234190.png")
        em.description = "**Gracias!**\nNos vemos pronto\n*Abierto 24/7*"
        await interaction.response.edit_message(embed=em, view=None)


class SellDropdown(discord.ui.Select):
    def __init__(self, pl: Player, bot: commands.Bot, what: str):
        self.pl = pl
        self.bot = bot
        self.what = what

        self.foco = (
            self.pl.animals
            if what == "animal"
            else self.pl.fishes
            if what == "fish"
            else self.pl.relics
        )

        options = [
            discord.SelectOption(
                label=f"x{self.foco[e]['quantity']:2} {self.foco[e][what]['name']} - {self.foco[e]['quantity']*self.foco[e][what]['value']:,} peniques",
                value=self.foco[e][what]["hash"],
            )
            for e in self.foco
        ]

        self.message: discord.Interaction
        super().__init__(placeholder="Que quieres vender?", options=options)

    async def callback(self, interaction: discord.Interaction):
        sel = self.values[0]
        obj = self.foco[sel]
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2372/2372853.png")

        if obj["quantity"] == 1:
            self.pl.pocket += obj[self.what]["value"]
            if self.what == "animal":
                self.pl.change_animal(Animal(**obj[self.what]), -1)
            elif self.what == "fish":
                self.pl.change_fish(Fish(**obj[self.what]), -1)
            else:
                self.pl.change_relic(Relic(**obj[self.what]), -1)
            self.pl.save()

            em.color = discord.Color.green()
            em.description = f"**Venta exitosa!**\n:{obj[self.what]['hash']}: `x{1}` por 🪙 `{obj[self.what]['value']*1:,}`\n*Quieres hacer algo más?*"

            await interaction.response.edit_message(
                embed=em,
                view=ShopAgain(self.pl, self.bot, "sell", self.what),
            )
        else:
            em.description = f"Cuantos quieres vender?\nTienes `x{obj['quantity']}` :{obj[self.what]['hash']}: disponibles\n`x1` :{obj[self.what]['hash']}: {obj[self.what]['name']} = `{obj[self.what]['value']:,}`"
            self.disabled = True

            await interaction.response.edit_message(
                embed=em,
                view=SellQty(self.pl, self.bot, self.what, sel),
            )


class SellQty(discord.ui.View):
    def __init__(self, pl: Player, bot: commands.Bot, what: str, item: str):
        self.pl = pl
        self.bot = bot
        self.what = what
        self.message: discord.Interaction
        super().__init__()
        self.add_item(SellQtyDropdown(pl, bot, what, item))

    @discord.ui.button(label="Inicio", style=discord.ButtonStyle.grey)
    async def home(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4634/4634649.png")

        em.description = "**Tienda**\nHola bienvenido,\nQue deseas hacer?"
        await interaction.response.edit_message(
            embed=em, view=ShopHome(self.pl, self.bot)
        )

    @discord.ui.button(label="Atras", style=discord.ButtonStyle.blurple)
    async def back(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2372/2372853.png")
        if self.what == "animal":
            em.description = f"\
:chicken: Pollo `10` peniques\n\
:hamster: Hamster `30` peniques\n\
:dog: Perro `40` peniques\n\
:cat: Gato `60` peniques\n\
:bird: Pájaro `80` peniques\n\
:rabbit: Conejo `100` peniques\n\
:monkey: Mono `150` peniques\n\
:fox: Zorro `200` peniques\n\
:wolf: Lobo `300` peniques\n\
:horse: Caballo `400` peniques\n\
:bear: Oso `500` peniques\n\
:elephant: Elefante `800` peniques\n\
:tiger: Tigre `1,000` peniques\n\
:lion: León `1,200` peniques\n\
:alien: Alien `1,500` peniques"
        elif self.what == "fish":
            em.description = f"\
:shell: Concha `10` peniques\n\
:shrimp: Camarón `30` peniques\n\
:fish: Charal `40` peniques\n\
:crab: Cangrejo `60` peniques\n\
:blowfish: Fogu `80` peniques\n\
:lobster: Langosta `100` peniques\n\
:turtle: Tortuga `150` peniques\n\
:otter: Nutria `200` peniques\n\
:seal: Foca `300` peniques\n\
:octopus: Pulpo `400` peniques\n\
:dolphin: Delfín `500` peniques\n\
:squid: Calamar `800` peniques\n\
:shark: Tiburón `1,000` peniques\n\
:whale: Ballena `1,200` peniques\n\
:sauropod: Nessie `1,500` peniques"
        else:
            em.description = f"\
:syringe: Jeringa `10` peniques\n\
:game_die: Dado `30` peniques\n\
:soccer: Balón `40` peniques\n\
:dart: Dardos `60` peniques\n\
:magic_wand: Varita `80` peniques\n\
:bell: Campana `100` peniques\n\
:lacrosse: Lacrosse `150` peniques\n\
:clock: Reloj `200` peniques\n\
:violin: Violín `300` peniques\n\
:trophy: Trofeo `400` peniques\n\
:rock: Piedra `500` peniques\n\
:bricks: Granito `800` peniques\n\
:diamond_shape_with_a_dot_inside: Turquesa `1,000` peniques\n\
:gem: Diamante `1,200` peniques\n\
:comet: Cometa `1,500` peniques"

        await interaction.response.edit_message(
            embed=em, view=Sell(self.pl, self.bot, self.what)
        )

    @discord.ui.button(label="Salir", style=discord.ButtonStyle.red)
    async def close(self, interaction: discord.Interaction, buton: discord.ui.Button):
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/1234/1234190.png")
        em.description = "**Gracias!**\nNos vemos pronto\n*Abierto 24/7*"
        await interaction.response.edit_message(embed=em, view=None)


class SellQtyDropdown(discord.ui.Select):
    def __init__(self, pl: Player, bot: commands.Bot, what: str, item: str):
        self.pl = pl
        self.bot = bot
        self.what = what
        self.item = item

        self.foco = (
            self.pl.animals
            if what == "animal"
            else self.pl.fishes
            if what == "fish"
            else self.pl.relics
        )

        options = [
            discord.SelectOption(
                label=f"x{i:2} {self.foco[item][what]['name']} - {i*self.foco[item][what]['value']:,}",
                value=f"{i}",
            )
            for i in range(self.foco[item]["quantity"], 0, -1)
        ]

        self.message: discord.Interaction
        super().__init__(placeholder="Cuantos quieres vender?", options=options)

    async def callback(self, interaction: discord.Interaction):
        sel = int(self.values[0])
        obj = self.foco[self.item]
        em = EcoEmbed(self.bot, self.pl.id)
        em.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2372/2372853.png")

        self.pl.pocket += obj[self.what]["value"] * sel
        if self.what == "animal":
            self.pl.change_animal(Animal(**obj[self.what]), -sel)
        elif self.what == "fish":
            self.pl.change_fish(Fish(**obj[self.what]), -sel)
        else:
            self.pl.change_relic(Relic(**obj[self.what]), -sel)
        self.pl.save()

        em.color = discord.Color.green()
        em.description = f"**Venta exitosa!**\n:{obj[self.what]['hash']}: `x{sel}` por 🪙 `{obj[self.what]['value']*sel:,}`\n*Quieres hacer algo más?*"

        await interaction.response.edit_message(
            embed=em,
            view=ShopAgain(self.pl, self.bot, "sell", self.what),
        )
