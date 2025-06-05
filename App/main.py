from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import routers_clinica

app = FastAPI(
    title="API Internacional - Clínica",
    description="API para gestionar información clínica",
    version="1.0.0"
)

# Middleware CORS opcional (si accedes desde frontend u otros servicios)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Reemplaza "*" por dominios específicos en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raíz opcional
@app.get("/", tags=["Inicio"], include_in_schema=False)
def read_root():
    return {"message": "Bienvenido a la API de DVZ Internacional"}

# Inclusión de rutas clínicas
app.include_router(routers_clinica.router, prefix="/api", tags=["Clínica"])
