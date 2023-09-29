from typing import Optional

import discord

from functions.playerload import playerload
from functions.playersearch import playersearch
from models import Player


def getplayer(user, member: Optional[discord.Member]) -> Player:
    if not member:
        id = user.id
        pl = playerload(id)
    else:
        id = member.id
        pl = playersearch(id)

    return pl
