from odmantic import Model
from bson import ObjectId
from typing import Optional

# Modelo para Libro
class Libro(Model):
    titulo: str
    autor_id: ObjectId
    descripcion: Optional[str]
    imagen_portada: Optional[str]
    inventario: int