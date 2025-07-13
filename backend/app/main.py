from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import pacientes, examen, orden, orden_examen

app = FastAPI(title="API Laboratorio Clínico")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pacientes.router)
app.include_router(examen.router)
app.include_router(orden.router)
app.include_router(orden_examen.router)