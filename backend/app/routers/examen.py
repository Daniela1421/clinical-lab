from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.examen import ExamenCreate, ExamenResponse
from app.crud import examen as examen_crud
from app.database import SessionLocal

router = APIRouter(prefix="/examenes", tags=["Examenes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ExamenResponse)
def crear_examen(examen: ExamenCreate, db: Session = Depends(get_db)):
    return examen_crud.crear_examen(db, examen)

@router.get("/", response_model=list[ExamenResponse])
def listar_examenes(db: Session = Depends(get_db)):
    return examen_crud.obtener_examenes(db)
