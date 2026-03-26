
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

def listar_arboles():
    if len(inventario) == 0:
        print("No hay árboles registrados.")
        return

    print("\n🌳 === INVENTARIO DE ÁRBOLES URBANOS ===")
    for i, arbol in enumerate(inventario, start=1):
        print(f"\nÁrbol #{i}")
        print(f"  Especie  : {arbol['especie']}")
        print(f"  Estado   : {arbol['estado']}")
        print(f"  Ubicación: {arbol['ubicacion']}")
    print("========================================\n")

