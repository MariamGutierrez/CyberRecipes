from fastapi.testclient import TestClient
from main import app  # Asegúrate de que `app` está expuesto en tu archivo principal

client = TestClient(app)

def test_procesar_links():
    response = client.post("/recetas/procesar_links/")
    assert response.status_code == 200
    assert "mensaje" in response.json()
    assert "procesaron" in response.json()["mensaje"]

def test_obtener_recetas():
    response = client.get("/recetas")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if response.json():  # Si hay recetas, validamos la estructura
        receta = response.json()[0]
        assert "nombre" in receta
        assert "ingredientes" in receta or "instrucciones" in receta

def test_obtener_receta_por_nombre():
    # Primero obtenemos una receta existente
    all_recetas = client.get("/recetas").json()
    if all_recetas:
        nombre = all_recetas[0]["nombre"]
        response = client.get(f"/receta/{nombre}")
        assert response.status_code == 200
        assert response.json()["nombre"] == nombre
    else:
        print("⚠️ No hay recetas cargadas en la base de datos para probar este endpoint.")
