from odmantic import Model
from datetime import datetime

class Prestamo(Model):
    lector_id: str  
    libro_id: str  
    fecha_prestamo: datetime
    fecha_devolucion: datetime 
    bibliotecario_id: str  
    foto_credencial:  str  