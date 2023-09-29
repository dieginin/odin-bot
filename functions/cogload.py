import os

from discord.ext import commands


async def cogload(bot: commands.Bot) -> int:
    cogs_loaded = 0

    for folder in ["commands", "events", "handlers"]:
        for filename in os.listdir(f"./{folder}"):
            if filename.endswith(".py"):
                try:
                    await bot.load_extension(f"{folder}.{filename[:-3]}")
                    cogs_loaded += 1
                except commands.ExtensionError as e:
                    print(f"Error al cargar la extensión {filename}: {str(e)}")

    return cogs_loaded
