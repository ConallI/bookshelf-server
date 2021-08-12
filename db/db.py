from pymongo import MongoClient
from config.config import *

client = MongoClient(
    get_mongo_connect_string(), tls=True, tlsAllowInvalidCertificates=True
)
db = client.get_default_database()


def get_user_by_name(name):
    return db.users.find_one({"name": name})


def get_user_by_name_and_password(name, password):
    return db.users.find_one({"name": name, "password": password})


def add_user(name, password):
    ret = get_user_by_name(name)
    if ret is None:
        new_user = {"name": name, "password": password, "bookmarks": {}}
        x = db.users.insert_one(new_user)
        ret = x.inserted_id

    return str(ret)


def add_cmd(name, password, cmd, url):
    new_cmd = db.users.update_one(
        {"name": name, "password": password}, {"$set": {f"bookmarks.{cmd}": url}}
    )
    return new_cmd.modified_count


def all_cmd(name, password):
    user = db.users.find_one({"name": name, "password": password})
    return user["bookmarks"]
