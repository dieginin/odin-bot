from connections import DBClient
from models import Player


def playerload(id: int) -> Player:
    client = DBClient("players")

    while True:
        pl = client.find(id)

        if pl:
            return pl

        client.insert(id, {"pocket": 100, "bank": 0})
