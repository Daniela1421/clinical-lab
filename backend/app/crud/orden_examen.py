from sqlalchemy.orm import Session
from app.models.orden_examen import OrdenExamen
from app.schemas.orden_examen import OrdenExamenCreate

def crear_orden_examen(db: Session, relacion: OrdenExamenCreate):
    db_relacion = OrdenExamen(**relacion.dict())
    db.add(db_relacion)
    db.commit()
    db.refresh(db_relacion)
    return db_relacion

def obtener_por_orden(db: Session, id_orden: int):
    return db.query(OrdenExamen).filter(OrdenExamen.id_orden == id_orden).all()
