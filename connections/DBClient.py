import pymongo

from config import DB_CLUSTER, DB_PASSWORD, DB_USER
from models import Player


class DBClient:
    def __init__(self, collection="players"):
        self.client = pymongo.MongoClient(
            f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_CLUSTER}/"
        )
        self.db = self.client["db"]
        self.col = self.db[collection]

    def insert(self, id: int, document):
        result = self.col.insert_one({"_id": id, **document})
        return result.inserted_id

    def find(self, id: int) -> Player | None:
        result = self.col.find_one({"_id": id})

        result = Player(**result) if result else None

        return result

    def update(self, id: int, update_data):
        result = self.col.update_one({"_id": id}, {"$set": update_data})
        return result.modified_count

    def delete(self, id: int):
        result = self.col.delete_one({"_id": id})
        return result.deleted_count

    def test(self) -> bool:
        try:
            self.client.admin.command("ping")
            return True
        except:
            return False
