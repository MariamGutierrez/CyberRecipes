import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from API.db.mongo import recetas_collection
from API.schemas.receta_schemas import RecetaBase
from API.db.mongo import recetas_collection, links_collection

def obtener_urls_de_recetas_lista() -> list[str]:
    lista_urls = []
    base_url = 'https://cookpad.com'
    url = 'https://cookpad.com/co/buscar/blog'

    resp = requests.get(url)
    if resp.status_code != 200:
        return lista_urls

    soup = BeautifulSoup(resp.text, 'html.parser')
    # Selector actualizado: clase block-link__main y atributo itemprop="url"
    enlaces = soup.select('a.block-link__main[itemprop="url"]')

    for enlace in enlaces:
        href = enlace.get('href')
        if href and href.startswith('/co/recetas/'):
            lista_urls.append(urljoin(base_url, href))

    return lista_urls


def obtener_receta_desde_url(url: str) -> RecetaBase | None:
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        print(f"Error {resp.status_code} en {url}")
        return None

    soup = BeautifulSoup(resp.text, 'html.parser')

    # Título
    titulo_tag = soup.find('h1')

    # Imagen
    imagen_tag = (
        soup.find('img', class_='photo')
        or soup.select_one('picture img')
    )

    # Ingredientes
    ingredientes = []
    for li in soup.select('li[id^="ingredient_"]'):
        texto = li.get_text(strip=True)
        if texto:
            ingredientes.append(texto)

    # Pasos
    pasos = []
    for li in soup.select('li[id^="step_"]'):
        texto = li.get_text(strip=True)
        if texto:
            pasos.append(texto)

    if not titulo_tag or not ingredientes or not pasos:
        print("No encontré alguno de los bloques en:", url)
        return None

    return RecetaBase(
        url         = url,
        nombre      = titulo_tag.get_text(strip=True),
        imagen      = imagen_tag.get('src') if imagen_tag else None,
        ingredientes= ingredientes,
        preparacion = pasos
    )





def scrapear_lista_y_guardar():
    for url in obtener_urls_de_recetas_lista():
        # 1) guardo la URL
        links_collection.insert_one({"url": url})
        
        # 2) scrappeo y guardo la receta
        receta = obtener_receta_desde_url(url)
        if receta:
            receta.model_dump(mode="json")

def procesar_links_y_guardar():
    """
    Toma cada URL de links_collection, extrae la receta con
    obtener_receta_desde_url, y la guarda en recetas_collection.
    Omite duplicados si ya existe una receta con esa misma URL.
    """
    for doc in links_collection.find({}, {"url": 1, "_id": 0}):
        url = doc["url"]
        
        # Omitir si ya la tenemos
        if recetas_collection.count_documents({"url": url}, limit=1):
            continue
        
        receta = obtener_receta_desde_url(url)
        if receta:
            # Añadimos la URL al dict antes de insertar
            data = receta.model_dump(mode="json")
            data["url"] = url
            result = recetas_collection.insert_one(data)
            print(f"Guardada receta '{receta.nombre}' (_id={result.inserted_id})")
        else:
            print(f"No se pudo scrapear {url}")

def guardar_link_de_receta(url: str):
    links_collection.insert_one({"url": url})

def guardar_receta(receta: RecetaBase):
    result = recetas_collection.insert_one(receta.model_dump(mode="json"))
    print(f"Insertada receta con _id={result.inserted_id}")




