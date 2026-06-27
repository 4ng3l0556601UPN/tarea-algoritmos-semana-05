# conversor.py

# Función que convierte grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):

    # Fórmula de conversión
    fahrenheit = (celsius * 9 / 5) + 32

    # Retornar el valor convertido
    return fahrenheit


# Función que convierte grados Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):

    # Fórmula de conversión
    celsius = (fahrenheit - 32) * 5 / 9

    # Retornar el valor convertido
    return celsius
