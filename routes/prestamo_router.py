from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from models.prestamo import Prestamo
from crud.prestamo_crud import create_loan, get_all_loans, get_loan_by_id, update_loan, delete_loan
from db.mongo import engine
from typing import Optional
from datetime import datetime

router = APIRouter()

@router.post("/prestamos/")
async def agregar_prestamo(
    lector_id: str = Form(...),
    libro_id: str = Form(...),
    fecha_prestamo: datetime = Form(...),
    bibliotecario_id: str = Form(...),
    archivo: UploadFile = File(...),
    ):
    
    response_create =  await create_loan(
        lector_id=lector_id, 
        libro_id=libro_id,
        fecha_prestamo=fecha_prestamo,
        bibliotecario_id=bibliotecario_id,
        archivo=archivo, 
        engine=engine
        )
    
    if response_create is None:
        return HTTPException(detail="Hubo un error al intentar crear el prestamo", status_code=400)
    else:
        return response_create

@router.get("/prestamos")
async def leer_prestamos():
    return await get_all_loans(engine)
    
@router.get("/prestamos/{loan_id}")
async def obtener_prestamo(loan_id: str):
    return await get_loan_by_id(loan_id, engine)

@router.put("/prestamos/{prestamo_id}")
async def editar_prestamo(
    prestamo_id: str,
    lector_id: str = Form(...),
    libro_id: str = Form(...),
    fecha_prestamo: datetime = Form(...),
    bibliotecario_id: str = Form(...),
    archivo: Optional[UploadFile] = File(None), 
):
    response_update = await update_loan(
        prestamo_id=prestamo_id,
        lector_id=lector_id,
        libro_id=libro_id,
        fecha_prestamo=fecha_prestamo,
        bibliotecario_id=bibliotecario_id,
        archivo=archivo,
        engine=engine
    )

    if response_update is None:
        raise HTTPException(detail="Hubo un error al intentar actualizar el préstamo", status_code=400)
    else:
        return response_update 
    
@router.delete("/prestamos/{prestamo_id}")
async def eliminar_prestamo(prestamo_id: str):
    response_delete = await delete_loan(prestamo_id=prestamo_id, engine=engine)
    
    if response_delete is None:
        raise HTTPException(detail="Hubo un error al intentar eliminar el préstamo", status_code=400)
    else:
        return response_delete  # Retornar el detalle de éxito