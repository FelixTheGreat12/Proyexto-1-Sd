from odmantic import AIOEngine, Model
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str = "mongodb://localhost:27017" 
    DATABASE_NAME: str = "BIBLIOTECA" 
settings = Settings()
 
client = AsyncIOMotorClient(settings.MONGODB_URI)
engine = AIOEngine(client=client, database=settings.DATABASE_NAME)

async def connect_db():
    # Conectar a la base de datos
    print("Connected to MongoDB")

async def close_db():
    # Cerrar la conexión a la base de datos
    client.close()
    print("Closed MongoDB connection")