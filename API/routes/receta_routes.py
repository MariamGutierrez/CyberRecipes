from fastapi import APIRouter, HTTPException
from API.schemas.receta_schemas import RecetaBase
from API.services.receta_service import obtener_receta_desde_url, guardar_receta, scrapear_lista_y_guardar, procesar_links_y_guardar
from API.db.mongo import recetas_collection
from fastapi import HTTPException
from bson.objectid import ObjectId

router = APIRouter()

# Permitir acceso desde cualquier origen (útil para desarrollo)


@router.post("/recetas/procesar_links/")
def endpoint_procesar_links():
    try:
        print("🔥 Ejecutando scraper en Heroku...")
        procesar_links_y_guardar()
        return {"mensaje": "Se procesaron y guardaron las recetas de todos los links"}
    except Exception as e:
        print("❌ Error al procesar links:", str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/recetas", response_model=list[RecetaBase])
def obtener_recetas():
    recetas = list(recetas_collection.find({}, {"_id": 0}))  # Excluir _id para evitar error de serialización
    return recetas

@router.get("/receta/{nombre}")
def obtener_receta_por_nombre(nombre: str):
    receta = recetas_collection.find_one({"nombre": nombre}, {"_id": 0})
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    return receta