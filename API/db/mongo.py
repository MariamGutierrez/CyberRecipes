import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    # Fuerza conexión inmediata para lanzar error si falla
    client.admin.command("ping")
    print("✅ Conectado a MongoDB Atlas con éxito.")
except Exception as e:
    print("❌ ERROR: No se pudo conectar a MongoDB Atlas.")
    print(str(e))
    raise e  # Esto detiene el deploy si estás usando Uvicorn o Heroku



