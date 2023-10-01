from copy import deepcopy
from typing import Literal

from connections import players


class Player:
    def __init__(
        self,
        _id: int,
        pocket: int,
        bank: int,
        tools: dict[Literal["bow_and_arrow", "fishing_pole_and_fish", "pick"], int],
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

    def change_tools(
        self,
        tool: Literal["bow_and_arrow", "fishing_pole_and_fish", "pick"],
        quantity: int,
    ):
        self.tools[tool] += quantity
