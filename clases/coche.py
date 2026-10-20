from pydantic import BaseModel, Field

# 1. Esquema de los datos de entrada del vehículo
class Coche(BaseModel):
    modelo: str = Field(min_length=2, max_length=40, description="Marca y modelo del coche")
    anio: int = Field(ge=1995, le=2026, description="Año de matriculación")
    km: int = Field(ge=0, le=500000, description="Kilómetros totales")
    precio_nuevo: float = Field(gt=3000, le=150000, description="Precio de compra nuevo")
    unico_dueno: bool = Field(default=True, description="Indica si ha tenido un solo dueño")