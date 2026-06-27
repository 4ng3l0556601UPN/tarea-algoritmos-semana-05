# Ordena la lista original con sort
def ordenar_lista(lista):
    lista.sort()

# Devuelve una copia ordenada
def copia_ordenada(lista):
    copia = []

    for elemento in lista:
        copia.append(elemento)

    copia.sort()
    return copia


# Programa principal
numeros = [8, 3, 5, 1, 7]

print("Lista original:", numeros)

copia = copia_ordenada(numeros)
print("Copia ordenada:", copia)
print("La lista original sigue igual:", numeros)

ordenar_lista(numeros)
print("Lista original ordenada:", numeros)
