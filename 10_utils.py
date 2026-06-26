def suma(*args):
    """Suma una cantidad variable de números."""
    return sum(args)

def promedio(*args):
    """Calcula el promedio de una cantidad variable de números."""
    if not args:
        return 0
    return sum(args) / len(args)

def informacion_persona(**kwargs):
    """Muestra información de una persona usando kwargs."""
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")

def ejecutar_funcion(func, *args, **kwargs):
    """Ejecuta cualquier función con argumentos variables."""
    return func(*args, **kwargs)

# Ejemplos de uso (puedes ponerlos en otro archivo o al final de utils.py)
if __name__ == "__main__":
    print("Suma:", suma(1, 2, 3, 4, 5))
    print("Promedio:", promedio(10, 20, 30))
    
    informacion_persona(nombre="Ana", edad=28, ciudad="Madrid")
    
    # Ejemplo de ejecutar_funcion
    resultado = ejecutar_funcion(suma, 100, 200, 300)
    print("Resultado con ejecutar_funcion:", resultado)