# data_manager.py - Tarea 2: Felipe Pautasso

inventario = []

def agregar_arbol(especie, estado, ubicacion):
    nuevo_arbol = {
        "especie": especie,
        "estado": estado,
        "ubicacion": ubicacion
    }
    inventario.append(nuevo_arbol)
    return f"Árbol '{especie}' agregado correctamente."
