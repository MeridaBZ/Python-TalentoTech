# Inventario de productos.
inventario = []

def mostrar_menu():
    print("\n--- SISTEMA DE GESTION DE INVENTARIO ---")
    print("Seleccione una opción:")
    print("1. Añadir un nuevo producto.")
    print("2. Mostrar todos los productos.")
    print("3. Actualizar la cantidad de un producto.")
    print("4. Eliminar un producto.")
    print("5. Reporte de productos con bajo stock.")
    print("6. Salir")

def leer_opcion():
    try:
        opcion = int(input(" --- INGRESE EL N° DE OPCION ---"))
        return opcion
    except ValueError:
        print("Por favor ingresa un número válido.")
        return None

def ejecutar_opcion(opcion):
    if opcion == 1:
        añadir_producto()
    elif opcion == 2:
        mostrar_inventario()
    elif opcion == 3:
        print("Actualizar el stock del producto...")
    elif opcion == 4:
        print("Eliminando un producto...")
    elif opcion == 5:
        print("Reporte de productos con bajo stock...")
    elif opcion == 6:
        print("Saliendo del sistema de inventario...")
    else:
        print("Opción no válida. Por favor elija otra opción.")

def añadir_producto():
    nombre = input("Ingresa el nombre del producto: ")
    try:
        cantidad = int(input("Ingresa la cantidad inicial del producto: "))
        inventario.append({"nombre": nombre, "cantidad": cantidad})
        print(f"Producto '{nombre}' añadido con cantidad {cantidad}.")
    except ValueError:
        print("Por favor, ingrese una cantidad válida.")

def mostrar_inventario():
    if inventario:
        print("\n--- INVENTARIO DE PRODUCTOS ---")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos registrados.")

while True:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 6:
        ejecutar_opcion(opcion)
        break
    elif opcion:
        ejecutar_opcion(opcion)
