from random import shuffle
# lista inicial
palitos =['_','__','___','____']


# funcion para mezclar los palitos
def mezclar(lista):
    shuffle(lista)
    return lista
print(mezclar(palitos))


# funcion que pide el intento al usuario

def probar_suerte():
    intento = ""

    while intento not in ["1","2","3","4"]:
        intento = input("Elige un numero entre el 1 y el 4: ")

    return int(intento)

# funcion para comprobar si lo escoge bien o no
def chequear_intento(lista,intento):
    if lista[intento - 1 ] == '-':
        print("TE MORISTE PUTO")
    else:
        print("TE SALVASTE PUTO")
    print(f" Te ha tocado {lista[intento - 1 ]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)