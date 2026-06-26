inventario = {}

def agregar_producto(nombre, cantidad):
    """Agrega o suma cantidad de un producto."""
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad
    print(f"✅ Agregado: {cantidad} unidades de {nombre}")

def actualizar_producto(nombre, cantidad):
    """Actualiza la cantidad de un producto (reemplaza)."""
    if nombre in inventario:
        inventario[nombre] = cantidad
        print(f"🔄 Actualizado: {nombre} = {cantidad}")
    else:
        print(f"❌ El producto '{nombre}' no existe en el inventario.")

def listar_inventario():
    """Muestra todo el inventario."""
    if not inventario:
        print("📭 El inventario está vacío.")
    else:
        print("\n📦 Inventario actual:")
        for producto, cantidad in inventario.items():
            print(f"   • {producto}: {cantidad} unidades")

agregar_producto("Laptop", 10)
agregar_producto("Mouse", 50)
actualizar_producto("Mouse", 45)
listar_inventario()