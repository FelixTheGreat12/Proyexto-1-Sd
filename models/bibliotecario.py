from odmantic import Model
from bson import ObjectId
from typing import Optional
from datetime import datetime

# Modelo para Bibliotecario
class Bibliotecario(Model):
    nombre: str
    apellido: str
    correo: str