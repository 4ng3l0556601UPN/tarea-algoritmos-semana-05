# Crear un diccionario vacío para guardar el inventario
inventario = {}



# Función para agregar productos al inventario
def agregar_producto(nombre, cantidad):

    # Agregar un nuevo elemento al diccionario
    inventario[nombre] = cantidad

    # Mostrar mensaje de confirmación
    print("Producto agregado:", nombre)



# Función para actualizar la cantidad de un producto
def actualizar_producto(nombre, cantidad):

    # Verificar si el producto existe usando el método in
    if nombre in inventario:

        # Actualizar el valor del producto
        inventario[nombre] = cantidad

        # Mostrar mensaje de actualización
        print("Producto actualizado:", nombre)

    else:

        # Mensaje si el producto no existe
        print("El producto no existe")



# Función para listar todos los productos
def listar_productos():

    # Usar el método items() para obtener clave y valor
    print("\nInventario:")

    for producto, cantidad in inventario.items():

        # Mostrar cada producto con su cantidad
        print(producto, "->", cantidad)



# Agregar productos
agregar_producto("Laptop", 5)
agregar_producto("Mouse", 20)
agregar_producto("Teclado", 10)



# Actualizar un producto existente
actualizar_producto("Mouse", 25)



# Mostrar todos los productos
listar_productos()