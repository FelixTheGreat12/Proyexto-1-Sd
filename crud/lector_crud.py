from models.lector import Lector
from odmantic import ObjectId
    
async def create_reader(lector: Lector, engine):
    await engine.save(lector)

async def get_all_readers(engine):
    return await engine.find(Lector)

async def get_reader(reader_id: str, engine):
    return await engine.find_one(Lector, Lector.id == ObjectId(reader_id))

async def update_reader(reader_id: str, reader_data: Lector, engine):
    reader = await get_reader(reader_id, engine)
    if reader:
        reader.nombre = reader_data.nombre
        reader.apellido = reader_data.apellido
        reader.correo = reader_data.correo
        await engine.save(reader)
        return reader
    return None

async def delete_reader(reader_id: str, engine):
    reader = await get_reader(reader_id, engine)
    if reader:
        await engine.delete(reader)
        return reader
    return None