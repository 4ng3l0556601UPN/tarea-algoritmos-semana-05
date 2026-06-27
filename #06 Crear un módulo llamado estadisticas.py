# Crear un módulo llamado estadisticas.py


# Crear función para calcular el promedio
def promedio(lista):

    # Sumar todos los valores de la lista
    suma = sum(lista)

    # Dividir la suma entre la cantidad de elementos
    resultado = suma / len(lista)

    # Retornar el promedio
    return resultado



# Crear función para obtener el valor máximo
def maximo(lista):

    # Usar max() para encontrar el número mayor
    mayor = max(lista)

    # Retornar el valor máximo
    return mayor



# Crear función para obtener el valor mínimo
def minimo(lista):

    # Usar min() para encontrar el número menor
    menor = min(lista)

    # Retornar el valor mínimo
    return menor