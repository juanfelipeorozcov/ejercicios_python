if __name__ == "__main__":
    a, b, c = 1, 2, 3
    print(a)
    print(b)
    print(c)
    d = 4, 5, 6
    print(d)
    e, f, g = d # destructurar - unpack
    print(e)
    h, *i = d # *i guarda los valores restantes (lista)
    print(i)

    *h, i = d
    print(i)

    *_, i = d # _ solo es una variable que no se va a usar
    print(i)


    # tarea = estudiar sobre paradigmas de programacion y pilas y colas
    # leer sobre el pep 8 