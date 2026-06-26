#Función agregar(lista, elemento) que añada el elemento al final de la lista
def agregar(lista, elemento):#.append() 
    lista.append(elemento)

#Creo una lista fuera de la función
mis_componentes = ["Teclado", "Mouse"]

#Se agrega la lista, en función  y el nuevo elemento
agregar(mis_componentes, "Monitor")

#Imprime la lista original fuera
print(mis_componentes)  
#Acá pasa con el nuevo elemento agregado ya que la función modifica y las listas son mutables