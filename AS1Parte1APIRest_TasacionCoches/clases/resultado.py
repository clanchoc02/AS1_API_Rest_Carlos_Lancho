from pydantic import BaseModel, Field

# 2. Esquema de la salida con el resultado de la tasación
class Resultado(BaseModel):
    valoracion: str = Field(description="Categoría o estado en el mercado")
    precio_estimado: float = Field(description="Precio calculado en euros")
    explicacion: str = Field(description="Resumen del cálculo realizado")