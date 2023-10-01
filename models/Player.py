from copy import deepcopy
from typing import Any, Literal

from connections import players
from models import Animal


class Player:
    def __init__(
        self,
        _id: int,
        pocket: int,
        bank: int,
        tools: dict[Literal["bow_and_arrow", "fishing_pole_and_fish", "pick"], int],
        animals: dict[str, dict[str, Any]],
    ):
        self.id = _id
        self.pocket = pocket
        self.bank = bank
        self.tools = tools
        self.animals = animals

    def save(self):
        self.animals = dict(
            sorted(self.animals.items(), key=lambda item: item[1]["animal"]["value"])
        )
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

    def change_animal(
        self,
        animal: Animal,
        quantity: int,
    ):
        if animal.hash in self.animals.keys():
            self.animals[animal.hash]["quantity"] += quantity
        else:
            self.animals[animal.hash] = {
                "animal": deepcopy(vars(animal)),
                "quantity": quantity,
            }
