from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class RecetaBase(BaseModel):
    url: HttpUrl                # ← Nuevo campo
    nombre: str
    imagen: Optional[HttpUrl]
    ingredientes: List[str]
    preparacion: List[str]

