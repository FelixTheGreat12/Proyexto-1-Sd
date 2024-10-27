from fastapi import APIRouter, HTTPException
from models.lector import Lector
from crud.lector_crud import create_reader, get_all_readers, get_reader, update_reader, delete_reader
from db.mongo import engine

router = APIRouter()

@router.post("/lectores/")
async def agregar_lector(lector: Lector):
    await create_reader(lector, engine)
    return lector

@router.get("/lectores")
async def leer_lectores():
    return await get_all_readers(engine)
    
@router.get("/lectores/{reader_id}")
async def leer_lector(reader_id: str):
    lector = await get_reader(reader_id, engine)
    if lector is None:
        return HTTPException(status_code=404, detail="No se encontró el lector")
    else:
        return lector
        

@router.put("/lectores/{reader_id}")
async def editar_lector(reader_id: str, lector: Lector):
    return await update_reader(reader_id, lector, engine)

@router.delete("/lectores/{reader_id}")
async def eliminar_lector(reader_id: str):
    return await delete_reader(reader_id, engine)