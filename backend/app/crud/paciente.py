from sqlalchemy.orm import Session
from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate

def crear_paciente(db: Session, paciente_data: PacienteCreate):
    paciente = Paciente(**paciente_data.dict())
    db.add(paciente)
    db.commit()
    db.refresh(paciente)
    return paciente

def obtener_paciente_por_documento(db: Session, documento: str):
    return db.query(Paciente).filter(Paciente.documento == documento).first()

def obtener_paciente_por_id(db: Session, paciente_id: int):
    return db.query(Paciente).filter(Paciente.id == paciente_id).first()

def listar_pacientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Paciente).offset(skip).limit(limit).all()
