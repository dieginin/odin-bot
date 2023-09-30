import pymongo

from config import DB_CLUSTER, DB_PASSWORD, DB_USER

client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_CLUSTER}/")


db = client["main"]
players = db["players"]


def test() -> bool:
    try:
        client.admin.command("ping")
        return True
    except:
        return False
