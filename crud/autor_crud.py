from models.autor import Autor
from odmantic import ObjectId
    
async def create_author(autor: Autor, engine):
    await engine.save(autor)

async def get_all_authors(engine):
    return await engine.find(Autor)

async def get_author(author_id: str, engine):
    return await engine.find_one(Autor, Autor.id == ObjectId(author_id))

async def update_author(author_id: str, author_data: Autor, engine):
    autor = await get_author(author_id, engine)
    if autor:
        autor.nombre = author_data.nombre
        autor.apellido = author_data.apellido
        autor.biografia = author_data.biografia if author_data.biografia else ""
        await engine.save(autor)
        return autor
    return None

async def delete_autor(author_id: str, engine):
    autor = await get_author(author_id, engine)
    if autor:
        await engine.delete(autor)
        return autor
    return None