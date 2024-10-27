from models.bibliotecario import Bibliotecario
from odmantic import ObjectId
    
async def create_librarian(bibliotecario: Bibliotecario, engine):
    await engine.save(bibliotecario)

async def get_all_librarians(engine):
    return await engine.find(Bibliotecario)

async def get_librarian(librarian_id: str, engine):
    return await engine.find_one(Bibliotecario, Bibliotecario.id == ObjectId(librarian_id))

async def update_librarian(librarian_id: str, librarian_data: Bibliotecario, engine):
    librarian = await get_librarian(librarian_id, engine)
    if librarian:
        librarian.nombre = librarian_data.nombre
        librarian.apellido = librarian_data.apellido
        librarian.correo = librarian_data.correo
        await engine.save(librarian)
        return librarian
    return None

async def delete_librarian(librarian_id: str, engine):
    librarian = await get_librarian(librarian_id, engine)
    if librarian:
        await engine.delete(librarian)
        return librarian
    return None