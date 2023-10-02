from copy import deepcopy
from typing import Any, Literal

from connections import players
from models import Animal, Fish


class Player:
    def __init__(
        self,
        _id: int,
        pocket: int,
        bank: int,
        tools: dict[Literal["bow_and_arrow", "fishing_pole_and_fish", "pick"], int],
        animals: dict[str, dict[str, Any]],
        fishes: dict[str, dict[str, Any]],
    ):
        self.id = _id
        self.pocket = pocket
        self.bank = bank
        self.tools = tools
        self.animals = animals
        self.fishes = fishes

    def save(self):
        self.animals = dict(
            sorted(self.animals.items(), key=lambda item: item[1]["animal"]["value"])
        )
        self.fishes = dict(
            sorted(self.fishes.items(), key=lambda item: item[1]["fish"]["value"])
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

    def change_fish(
        self,
        fish: Fish,
        quantity: int,
    ):
        if fish.hash in self.fishes.keys():
            self.fishes[fish.hash]["quantity"] += quantity
        else:
            self.fishes[fish.hash] = {
                "fish": deepcopy(vars(fish)),
                "quantity": quantity,
            }
