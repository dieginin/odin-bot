from connections import DBClient
from models import Player


def playersearch(id: int) -> Player:
    client = DBClient("players")

    pl = client.find(id)

    if pl:
        return pl
    else:
        return Player(id, 0, 0)
