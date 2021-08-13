from pymongo import MongoClient
import random
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
    key = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFHJKLZXCVBNM1234567890")
    random.shuffle(key)
    api_key = "".join(key)
    if ret is None:
        new_user = {
            "name": name,
            "password": password,
            "bookmarks": {},
            "apiKey": api_key,
        }
        x = db.users.insert_one(new_user)
        ret = get_user_by_name_and_password(name, password)

    return ret


def all_cmd(key):
    user = db.users.find_one({"apiKey": key})
    return user["bookmarks"]


def add_cmd(key, cmd, url):
    new_cmd = db.users.update_one({"key": key}, {"$set": {f"bookmarks.{cmd}": url}})
    return new_cmd.modified_count


def del_cmd(key, cmd):
    new_cmd = db.users.update_one({"key": key}, {"$unset": {f"bookmarks.{cmd}"}})
    return new_cmd.modified_count
