from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.schemas.paciente import Paciente, PacienteCreate
from app.crud import paciente as crud_paciente

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Paciente)
def crear_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    db_paciente = crud_paciente.obtener_paciente_por_documento(db, paciente.documento)
    if db_paciente:
        raise HTTPException(status_code=400, detail="El documento ya está registrado.")
    return crud_paciente.crear_paciente(db, paciente)

@router.get("/documento/{documento}", response_model=Paciente)
def obtener_paciente(documento: str, db: Session = Depends(get_db)):
    db_paciente = crud_paciente.obtener_paciente_por_documento(db, documento)
    if not db_paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado.")
    return db_paciente

@router.get("/", response_model=List[Paciente])
def listar_pacientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_paciente.listar_pacientes(db, skip=skip, limit=limit)
