from fastapi import APIRouter, HTTPException
from models.bibliotecario import Bibliotecario
from crud.bibliotecario_crud import create_librarian, get_all_librarians, get_librarian, update_librarian, delete_librarian
from db.mongo import engine

router = APIRouter()

@router.post("/bibliotecarios/")
async def agregar_bibliotecario(bibliotecario: Bibliotecario):
    await create_librarian(bibliotecario, engine)
    return bibliotecario

@router.get("/bibliotecarios")
async def leer_bibliotecarios():
    return await get_all_librarians(engine)
    
@router.get("/bibliotecarios/{librarian_id}")
async def leer_bibliotecario(librarian_id: str):
    bibliotecario = await get_librarian(librarian_id, engine)
    if bibliotecario is None:
        return HTTPException(status_code=404, detail="No se encontró el bibliotecario")
    else:
        return bibliotecario
        

@router.put("/bibliotecarios/{librarian_id}")
async def editar_bibliotecario(librarian_id: str, bibliotecario: Bibliotecario):
    return await update_librarian(librarian_id, bibliotecario, engine)

@router.delete("/bibliotecarios/{librarian_id}")
async def eliminar_bibliotecario(librarian_id: str):
    return await delete_librarian(librarian_id, engine)