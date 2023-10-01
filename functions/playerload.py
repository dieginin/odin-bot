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
                "tools": {"bow": 1, "rod": 1, "pick": 1},
            }
        )
