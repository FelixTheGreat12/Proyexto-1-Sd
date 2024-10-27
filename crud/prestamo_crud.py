from models.prestamo import Prestamo
from odmantic import ObjectId
from helpers.helpers import upload_file, delete_file
from fastapi import UploadFile, HTTPException
from typing import Optional
from datetime import timedelta, datetime
from crud.libro_crud import get_libro, update_libro
    
bucket = "biblioteca-sd"

# Crear un nuevo préstamo
async def create_loan(
    lector_id: str,
    libro_id: str,
    fecha_prestamo: str,
    bibliotecario_id: str,
    archivo: UploadFile,
    fecha_devolucion: Optional[str] = None,
    engine = None, 
):
    libro = await get_libro(libro_id, engine=engine)
    
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
    # Validamos existencias
    if libro.inventario == 0:
        raise HTTPException(status_code=400, detail="El libro no está disponible")

    # Obtener URL del archivo en S3
    file_url_response = await upload_file(file=archivo, bucket=bucket, path="prestamos")
    
    if "url" in file_url_response:
        foto_credencial = file_url_response["url"]
        # Agregamos la fecha de devolucion
        fecha_devolucion = fecha_prestamo + timedelta(days=3)
        
        libro.inventario -= 1  # Disminuir el inventario
        
        await update_libro(libro_data=libro, libro_id=libro_id, engine=engine)
        
        # Objeto préstamo
        prestamo = Prestamo(
            lector_id=lector_id,
            libro_id=libro_id,
            fecha_prestamo=fecha_prestamo,
            fecha_devolucion=fecha_devolucion,
            bibliotecario_id=bibliotecario_id,
            foto_credencial=foto_credencial
        )

        return await engine.save(prestamo)
    else:
        raise HTTPException(status_code=500, detail="Error al subir la imagen")

# Obtener todos los préstamos
async def get_all_loans(engine):
    return await engine.find(Prestamo)

# Obtener un préstamo por ID
async def get_loan_by_id(loan_id: str, engine):
    loan = await engine.find_one(Prestamo, Prestamo.id == ObjectId(loan_id))
    if loan is None:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return loan

async def update_loan(
    prestamo_id: str,
    lector_id: str,
    libro_id: str,
    fecha_prestamo: datetime,
    bibliotecario_id: str,
    archivo: Optional[UploadFile] = None,
    engine = None,
):
    prestamo = await engine.find_one(Prestamo, Prestamo.id == ObjectId(prestamo_id))

    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")

    libro = await get_libro(libro_id, engine=engine)

    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    # Validamos existencias
    if libro.inventario == 0:
        raise HTTPException(status_code=400, detail="El libro no está disponible")

    # Si se proporciona un nuevo archivo, manejamos la actualización de la imagen
    if archivo:
        # Obtener la URL existente de la foto de credencial
        existing_file_url = prestamo.foto_credencial
        # Extraer el nombre del archivo de la URL
        existing_file_name = existing_file_url.split('/')[-1]

        # Eliminar la imagen existente de S3
        await delete_file(bucket, "prestamos", existing_file_name)

        # Subir la nueva imagen a S3
        file_url_response = await upload_file(file=archivo, bucket=bucket, path="prestamos")

        if "url" in file_url_response:
            prestamo.foto_credencial = file_url_response["url"]  # Actualizar la URL con la nueva imagen

    # Actualizamos otros campos del préstamo
    prestamo.lector_id = lector_id
    prestamo.libro_id = libro_id
    prestamo.fecha_prestamo = fecha_prestamo
    prestamo.bibliotecario_id = bibliotecario_id
    prestamo.fecha_devolucion = fecha_prestamo + timedelta(days=3)  # Default a 3 días después

    # Guardar los cambios en la base de datos
    await engine.save(prestamo)

    return prestamo

async def delete_loan(prestamo_id: str, engine):
    # Buscar el préstamo por ID
    prestamo = await engine.find_one(Prestamo, Prestamo.id == ObjectId(prestamo_id))
    
    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")

    # Eliminar el archivo de S3 si existe
    if prestamo.foto_credencial:

        existing_file_url = prestamo.foto_credencial

        existing_file_name = existing_file_url.split('/')[-1]

        await delete_file(bucket, "prestamos", existing_file_name)

    # Eliminar el préstamo de la base de datos
    await engine.delete(prestamo)
    return {"detail": "Préstamo eliminado con éxito"}