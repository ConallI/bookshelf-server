import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_mongo_connect_string():
    return os.environ.get("MONGO_CONNECT_STRING", "")
