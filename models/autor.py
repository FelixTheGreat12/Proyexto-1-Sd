from odmantic import Model
from typing import Optional

# Modelo para Autor
class Autor(Model):
    nombre: str
    apellido: str
    biografia: Optional[str]