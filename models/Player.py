from copy import deepcopy
from typing import Literal

from connections import players


class Player:
    def __init__(
        self,
        _id: int,
        pocket: int,
        bank: int,
        tools: dict[Literal["bow_and_arrow", "rod", "pick"], int],
    ):
        self.id = _id
        self.pocket = pocket
        self.bank = bank
        self.tools = tools

    def save(self):
        character_dict = deepcopy(vars(self))
        character_dict.pop("id")

        result = players.update_one({"_id": self.id}, {"$set": character_dict})
        return result.modified_count
