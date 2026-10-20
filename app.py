from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from clases.coche import Coche
from clases.resultado import Resultado
from funciones.calculos import calcular_tasacion

app = FastAPI(
    title="Servicio de Tasación de Vehículos",
    description="API para estimar el valor de coches de segunda mano",
    version="1.0.0"
)

# Configuración de CORSMiddleware para conectar con el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Permite peticiones desde cualquier origen (ideal en desarrollo)
    allow_credentials=True,
    allow_methods=["*"],        # Permite todos los métodos HTTP (GET, POST, OPTIONS...)
    allow_headers=["*"],        # Permite todas las cabeceras (Content-Type, etc.)
)

# Montamos la carpeta static para servir el código JavaScript y estilos
app.mount("/static", StaticFiles(directory="static"), name="static")

# 1. Definimos el endpoint GET de la página principal
@app.get("/", response_class=FileResponse)
def estado_servicio():
    """
    Reenvía a la página de inicio.
    """
    return FileResponse("index.html")

# 2. Definimos el endpoint POST de inferencia
@app.post("/tasar-coche", response_model=Resultado)
def tasar_coche(coche: Coche):
    """
    Recibe los datos del vehículo y calcula una estimación de su precio.
    """
    return calcular_tasacion(coche)