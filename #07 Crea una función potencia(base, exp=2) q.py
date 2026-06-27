# Crear una función llamada potencia
# El parámetro exp tiene un valor por defecto de 2
def potencia(base, exp=2):

    # Calcular la potencia usando el operador **
    resultado = base ** exp

    # Retornar el resultado
    return resultado



# Usar la función indicando solamente la base
# Como no enviamos exp, usará el valor por defecto 2
resultado1 = potencia(5)


# Mostrar resultado
print("5 elevado al cuadrado es:", resultado1)



# Usar la función enviando base y exponente
resultado2 = potencia(3, 4)


# Mostrar resultado
print("3 elevado a la 4 es:", resultado2)