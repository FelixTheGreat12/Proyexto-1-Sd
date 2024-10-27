from odmantic import Model

# Modelo para Lector
class Lector(Model):
    nombre: str
    apellido: str
    correo: str