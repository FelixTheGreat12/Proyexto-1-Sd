from fastapi import FastAPI 
from db.mongo import connect_db, close_db
from routes.libro_router import router as libro_router
from routes.autor_router import router as autor_router
from routes.bibliotecario_router import router as bibliotecario_router
from routes.lector_router import router as lector_router
from routes.prestamo_router import router as prestamo_router

app = FastAPI()
custom_prefix = "/api/v1"

@app.on_event("startup")
async def startup_event():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_event():
    await close_db()

app.include_router(libro_router, prefix=custom_prefix)
app.include_router(autor_router, prefix=custom_prefix)
app.include_router(bibliotecario_router, prefix=custom_prefix)
app.include_router(lector_router, prefix=custom_prefix)
app.include_router(prestamo_router, prefix=custom_prefix)