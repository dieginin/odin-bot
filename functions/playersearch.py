from connections import players
from models import Player


def playersearch(id: int) -> Player:
    result = players.find_one({"_id": id})

    return Player(**result) if result else Player(id, 0, 0)
