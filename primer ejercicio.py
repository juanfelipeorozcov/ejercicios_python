def hanoi (n,origen,destino,auxiliar):
    if n == 1:
        print (f"mueve el disco 1 de {origen} a {destino}")
        return
    hanoi(n-1, origen, auxiliar, destino)
    print(f"mueve el disco {n} de {origen} a {destino}")
    hanoi(n-1, auxiliar, destino, origen)


n = 3
hanoi(n,"A","B","C")
