from fastapi import APIRouter, HTTPException
from models.autor import Autor
from crud.autor_crud import create_author, get_all_authors, get_author, update_author, delete_autor
from db.mongo import engine

router = APIRouter()

@router.post("/autores/")
async def agregar_autor(autor: Autor):
    await create_author(autor, engine)
    return autor

@router.get("/autores")
async def leer_autores():
    return await get_all_authors(engine)
    
@router.get("/autores/{author_id}")
async def leer_autor(author_id: str):
    autor = await get_author(author_id, engine)
    if autor is None:
        return HTTPException(status_code=404, detail="No se encontró el autor")
    else:
        return autor
        

@router.put("/autores/{author_id}")
async def editar_autor(author_id: str, autor: Autor):
    return await update_author(author_id, autor, engine)

@router.delete("/autores/{author_id}")
async def eliminar_autor(author_id: str):
    return await delete_autor(author_id, engine)