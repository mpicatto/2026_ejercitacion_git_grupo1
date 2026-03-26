
# More 

from data_manager import inicializar_datos

inicializar_datos()

while True:
    print("--- Eco-Tracker Las Varillas ---") 
    print("1. Ver árboles")
    print("2. Agregar árbol")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Función de listar árboles aún no implementada")
    
    elif opcion == "2":
        print("Función de agregar árbol aún no implementada")
    
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción inválida")

# Alumno 4: Faustino
from data_manager import inicializar_datos, listar_arboles

def main():
    inicializar_datos()

    while True:
        print("\n M-? ECO-TRACKER LAS VARILLAS")
        print("1. Ver árboles")
        print("2. Agregar árbol")
        print("3. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            listar_arboles()
        elif opcion == "2":
            print("(Función en desarrollo...)")
        elif opcion == "3":
            print("¡Hasta luego!  M-1")
            break
        else:
            print("Opción no válida, intentá de nuevo.")

if __name__ == "__main__":
    main()



