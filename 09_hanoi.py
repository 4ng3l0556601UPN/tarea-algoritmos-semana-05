def hanoi(n, origen, destino, auxiliar):
    """
    Resuelve el problema de las Torres de Hanói.
    n: número de discos
    origen, destino, auxiliar: nombres de las torres (strings)
    """
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    
    # Mover n-1 discos a la torre auxiliar
    hanoi(n-1, origen, auxiliar, destino)
    
    # Mover el disco n a la torre destino
    print(f"Mover disco {n} de {origen} a {destino}")
    
    # Mover los n-1 discos de auxiliar a destino
    hanoi(n-1, auxiliar, destino, origen)

# Ejemplo de uso:
print("🔧 Solución Torres de Hanói con 3 discos:")
hanoi(3, "A", "C", "B")