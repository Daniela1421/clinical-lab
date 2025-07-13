from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.orden_examen import OrdenExamenCreate, OrdenExamenResponse
from app.crud import orden_examen as crud_orden_examen

router = APIRouter(prefix="/ordenes-examenes", tags=["OrdenExamen"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrdenExamenResponse)
def crear_relacion_orden_examen(relacion: OrdenExamenCreate, db: Session = Depends(get_db)):
    return crud_orden_examen.crear_orden_examen(db, relacion)

@router.get("/orden/{id_orden}", response_model=list[OrdenExamenResponse])
def obtener_examenes_por_orden(id_orden: int, db: Session = Depends(get_db)):
    return crud_orden_examen.obtener_por_orden(db, id_orden)
