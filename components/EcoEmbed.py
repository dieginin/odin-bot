import discord
from discord.ext import commands


def EcoEmbed(bot: commands.Bot, id: int) -> discord.Embed:
    member = discord.utils.get(bot.get_all_members(), id=id)
    embed = discord.Embed(color=discord.Color.random())
    if member:
        embed.set_author(name=member.display_name, icon_url=member.display_avatar.url)
    return embed
