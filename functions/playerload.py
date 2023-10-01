from connections import players
from models import Player


def playerload(id: int) -> Player:
    while True:
        result = players.find_one({"_id": id})

        if result:
            return Player(**result)

        players.insert_one(
            {
                "_id": id,
                "pocket": 100,
                "bank": 0,
                "tools": {"bow_and_arrow": 1, "fishing_pole_and_fish": 1, "pick": 1},
            }
        )
