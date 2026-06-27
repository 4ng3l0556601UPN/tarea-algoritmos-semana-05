# Función que ordena la lista original (modifica la lista existente)
def ordenar_referencia(lista):

    # Usar sort() para ordenar la misma lista
    lista.sort()

    # Retornar la lista ya ordenada
    return lista



# Función que devuelve una copia ordenada sin modificar la original
def devolver_copia_ordenada(lista):

    # Crear una copia de la lista original
    copia = lista.copy()

    # Ordenar la copia
    copia.sort()

    # Retornar la nueva lista ordenada
    return copia


# Crear una lista de ejemplo
numeros = [8, 3, 5, 1, 9]

# Mostrar lista original
print("Lista original:", numeros)


# Llamar función que modifica la lista original
ordenar_referencia(numeros)


# Mostrar lista después de ordenar por referencia
print("Lista ordenada original:", numeros)


# Crear otra lista de ejemplo
numeros2 = [7, 4, 6, 2, 10]


# Mostrar segunda lista original
print("Segunda lista original:", numeros2)



# Llamar función que devuelve una copia ordenada
nueva_lista = devolver_copia_ordenada(numeros2)


# Mostrar copia ordenada
print("Copia ordenada:", nueva_lista)


# Mostrar que la lista original sigue igual
print("Lista original sin cambios:", numeros2)
