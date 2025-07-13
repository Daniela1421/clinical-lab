from sqlalchemy.orm import Session
from app.models.examen import Examen
from app.schemas.examen import ExamenCreate

def crear_examen(db: Session, examen: ExamenCreate):
    db_examen = Examen(**examen.dict())
    db.add(db_examen)
    db.commit()
    db.refresh(db_examen)
    return db_examen

def obtener_examenes(db: Session):
    return db.query(Examen).all()
