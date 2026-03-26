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
