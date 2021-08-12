from pymongo import MongoClient

from config.config import *

client = MongoClient(
    get_mongo_connect_string(), tls=True, tlsAllowInvalidCertificates=True
)
db = client.get_default_database()


def get_user_by_name(name):
    return db.users.find_one({"name": name})


def add_user(name, password):

    ret = get_user_by_name(name)

    if ret is None:
        new_user = {"name": name, "password": password, "bookmarks": {}}
        x = db.users.insert_one(new_user)
        ret = x.inserted_id

    return str(ret)
