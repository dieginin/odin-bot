import os

from discord.ext import commands


async def cogload(bot: commands.Bot) -> str:
    cogs_loaded = []

    for folder in ["commands", "handlers"]:
        for filename in os.listdir(f"./{folder}"):
            if filename.endswith(".py"):
                try:
                    await bot.load_extension(f"{folder}.{filename[:-3]}")
                    cogs_loaded.append(f"{filename[:-3]}")
                except commands.ExtensionError as e:
                    print(f"Error al cargar la extensión {filename}: {str(e)}")

    return ", ".join(cogs_loaded)
