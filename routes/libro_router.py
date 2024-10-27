from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from models.libro import Libro
from crud.libro_crud import create_libro, get_all_libros, get_libro, update_libro, delete_libro
from db.mongo import engine
from typing import Optional

router = APIRouter()

@router.post("/libros/")
async def agregar_libro(
    titulo: str = Form(...),
    autor_id: str = Form(...),
    descripcion: str = Form(...),
    inventario: int = Form(...),
    archivo: UploadFile = File(...),
    ):
    
    response_create = await create_libro(
        titulo=titulo, 
        autor_id=autor_id,
        descripcion=descripcion,
        inventario=inventario,
        archivo=archivo,
        engine=engine
        )
    
    if response_create is None:
        return HTTPException(detail="Hubo un error al intentar crear el libro", status_code=400)
    else:
        return response_create

@router.get("/libros")
async def leer_libros():
    return await get_all_libros(engine)
    
@router.get("/libros/{libro_id}")
async def leer_libro(libro_id: str):
    libro = await get_libro(libro_id, engine)
    if libro is None:
        return HTTPException(status_code=404, detail="No se encontró el libro")
    else:
        return libro
        

@router.put("/libros/{libro_id}")
async def editar_libro(
    libro_id: str,
    titulo: str = Form(...),
    autor_id: str = Form(...),
    descripcion: str = Form(...),
    inventario: int = Form(...),
    archivo: Optional[UploadFile] = File(None),
    ):
    
    response_update = await update_libro(
        libro_id, 
        autor_id=autor_id,
        titulo=titulo,
        descripcion=descripcion,
        inventario=inventario,
        archivo=archivo,
        engine=engine
        )
    
    if response_update is None:
        raise HTTPException(detail="Hubo un error al intentar actualizar el libro", status_code=400)
    else:
        return response_update 

@router.delete("/libros/{libro_id}")
async def eliminar_libro(libro_id: str):
    response_delete =  await delete_libro(libro_id, engine)
    
    if response_delete is None:
        raise HTTPException(detail="Hubo un error al intentar eliminar el libro", status_code=400)
    else:
        return response_delete  # Retornar el detalle de éxito