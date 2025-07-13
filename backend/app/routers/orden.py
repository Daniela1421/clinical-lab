from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.orden import OrdenCreate, OrdenResponse
from app.models.paciente import Paciente
from app.crud import orden as orden_crud

router = APIRouter(prefix="/ordenes", tags=["Ordenes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrdenResponse)
def crear_orden(orden: OrdenCreate, db: Session = Depends(get_db)):
    return orden_crud.crear_orden(db, orden)

@router.get("/paciente/{documento}", response_model=list[OrdenResponse])
def listar_ordenes_por_documento(documento: str, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.documento == documento).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return orden_crud.obtener_orden_por_documento(db, documento)

@router.get("/{orden_id}", response_model=OrdenResponse)
def obtener_detalle_orden(orden_id: int, db: Session = Depends(get_db)):
    orden = orden_crud.obtener_orden(db, orden_id)
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return orden
