#Calcular un cuadrado entero que retorne valor y se muestre

def cuadrado(n):
    cal_local = n ** 2  #Name para el entorno local
    return cal_local #retornarà el calculo local sin esto solo aparecería none

numero = int(input("Insertar número entero: "))  #Name único global
resultado_final = cuadrado(numero)

print(f"El cuadrado del {numero} es: {resultado_final}")