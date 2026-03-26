# Alumno 1 - Emi  

# Lista global donde se guardan los árboles
inventario = []

def inicializar_datos():
    global inventario

    arbol1 = {
        "especie": "Jacarandá",
        "estado": "Saludable",
        "ubicacion": "Plaza central"
    }

    arbol2 = {
        "especie": "Pino",
        "estado": "Enfermo",
        "ubicacion": "Avenida San Martín"
    }

    arbol3 = {
        "especie": "Lapacho",
        "estado": "Saludable",
        "ubicacion": "Parque municipal"
    }

    inventario = [arbol1, arbol2, arbol3]
