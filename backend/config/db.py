from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
mongo_connection_string = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@localhost:27017/"

client = MongoClient(mongo_connection_string)

db = client[DATABASE_NAME]
