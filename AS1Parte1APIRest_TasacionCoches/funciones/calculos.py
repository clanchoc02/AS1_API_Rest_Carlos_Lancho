from clases.coche import Coche

# Función para calcular la tasacion de un coche
def calcular_tasacion(coche: Coche):
    edad = 2026 - coche.anio
    
    precio = coche.precio_nuevo * (1 - (edad * 0.06))
    precio = precio - (coche.km * 0.02)

    if coche.unico_dueno:
        precio = precio + 500

    if precio < 600:
        precio = 600.0
    
    precio_final = round(precio, 2)

    valoracion = "Bastante desgaste"

    if precio_final > (coche.precio_nuevo * 0.5):
        valoracion = "Buena ocasión"
    elif precio_final > (coche.precio_nuevo * 0.25):
        valoracion = "Precio normal"

    mensaje = f"Coche {coche.modelo} con {edad} años y {coche.km} km."

    return {
        "valoracion": valoracion,
        "precio_estimado": precio_final,
        "explicacion": mensaje
    }