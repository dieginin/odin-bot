from copy import deepcopy
from typing import Any, Literal

from connections import players
from models import Animal, Fish, Relic


class Player:
    def __init__(
        self,
        _id: int,
        pocket: int,
        bank: int,
        tools: dict[Literal["bow_and_arrow", "fishing_pole_and_fish", "pick"], int],
        animals: dict[str, dict[str, Any]],
        fishes: dict[str, dict[str, Any]],
        relics: dict[str, dict[str, Any]],
    ):
        self.id = _id
        self.pocket = pocket
        self.bank = bank
        self.tools = tools
        self.animals = animals
        self.fishes = fishes
        self.relics = relics

    def save(self):
        self.animals = dict(
            sorted(self.animals.items(), key=lambda item: item[1]["animal"]["value"])
        )
        self.fishes = dict(
            sorted(self.fishes.items(), key=lambda item: item[1]["fish"]["value"])
        )
        self.relics = dict(
            sorted(self.relics.items(), key=lambda item: item[1]["relic"]["value"])
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
        if self.animals[animal.hash]["quantity"] == 0:
            self.animals.pop(animal.hash)

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
        if self.fishes[fish.hash]["quantity"] == 0:
            self.fishes.pop(fish.hash)

    def change_relic(
        self,
        relic: Relic,
        quantity: int,
    ):
        if relic.hash in self.relics.keys():
            self.relics[relic.hash]["quantity"] += quantity
        else:
            self.relics[relic.hash] = {
                "relic": deepcopy(vars(relic)),
                "quantity": quantity,
            }
        if self.relics[relic.hash]["quantity"] == 0:
            self.relics.pop(relic.hash)
