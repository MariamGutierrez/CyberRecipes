import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # carga MONGO_URI de tu .env

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

# 1) Seleccionas la base de datos "recetas"
db = client["recetas"]

# 2) Seleccionas la colección dentro de esa DB.
#    Cámbialo por "links-recetas" o por "re-list" según lo que quieras poblar.
links_collection = db["links-recetas"]
recetas_collection = db["re-list"]


