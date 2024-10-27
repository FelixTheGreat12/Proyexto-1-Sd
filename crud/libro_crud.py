from models.libro import Libro
from odmantic import ObjectId
from fastapi import UploadFile, HTTPException
from helpers.helpers import upload_file, delete_file
from typing import Optional

bucket = "biblioteca-sd"

async def create_libro(
    titulo: str,
    autor_id: str,
    descripcion: str,
    inventario: int,
    archivo: UploadFile,
    engine
    ):
    
    # Obtener URL del archivo en S3
    file_url_response = await upload_file(file=archivo, bucket=bucket, path="libros")
    
    if "url" in file_url_response:
        imagen_portada = file_url_response["url"]
        
        # Objeto préstamo
        libro = Libro(
            titulo=titulo,
            autor_id=autor_id,
            descripcion=descripcion,
            inventario=inventario,
            imagen_portada=imagen_portada
        )

        return await engine.save(libro)
    else:
        raise HTTPException(status_code=500, detail="Error al subir la imagen")


async def get_all_libros(engine):
    return await engine.find(Libro)

async def get_libro(libro_id: str, engine):
    return await engine.find_one(Libro, Libro.id == ObjectId(libro_id))

async def update_libro(
    libro_id: int,  
    titulo: str,
    autor_id: str,
    descripcion: str,
    inventario: int,
    archivo: Optional[UploadFile] = None,
    engine = None
    ):
    
    libro = await get_libro(libro_id, engine)
    
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
    # Si se proporciona un nuevo archivo, manejamos la actualización de la imagen
    if archivo:
        # Obtener la URL existente de la foto de credencial
        existing_file_url = libro.imagen_portada
        # Extraer el nombre del archivo de la URL
        existing_file_name = existing_file_url.split('/')[-1]

        # Eliminar la imagen existente de S3
        await delete_file(bucket, "libros", existing_file_name)

        # Subir la nueva imagen a S3
        file_url_response = await upload_file(file=archivo, bucket=bucket, path="libros")

        if "url" in file_url_response:
            libro.imagen_portada = file_url_response["url"]  # Actualizar la URL con la nueva imagen
        else:
            raise HTTPException(status_code=500, detail="Error al subir la imagen")
        
    # Actualizamos otros campos del préstamo
    libro.titulo = titulo
    libro.autor_id = autor_id
    libro.descripcion = descripcion
    libro.inventario = inventario  # Default a 3 días después

    # Guardar los cambios en la base de datos
    await engine.save(libro)

    return libro

async def delete_libro(libro_id: int, engine):
   # Buscar el préstamo por ID
    libro = await engine.find_one(Libro, Libro.id == ObjectId(libro_id))
    
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    # Eliminar el archivo de S3 si existe
    if libro.imagen_portada:

        existing_file_url = libro.imagen_portada

        existing_file_name = existing_file_url.split('/')[-1]

        await delete_file(bucket, "libros", existing_file_name)

    # Eliminar el préstamo de la base de datos
    await engine.delete(libro)
    return {"detail": "Libro eliminado con éxito"}