from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_URI)

db = client["recetas"]

links_collection = db["links-recetas"]
recetas_collection = db["re-list"]  # 👈 ESTA debe existir




