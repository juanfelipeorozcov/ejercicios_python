# usar el metodo choice  (selecciona algo de la lista de forma aleatoria)
# funciones para pedir : letras, validar letras, chequearletras, ver si gano
# 1o funciones y luego implementación


from random import choice

palabras = ["cabernicola","murcielago","dinosaurio"]
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palabras(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))  # el set no permite elementos duplicados los ignora

    return palabra_elegida,letras_unicas


def pedir_letra():
    letra_elegida = ""
    es_valida = False
    abecedario = "abcdefghijklmnopqrstuwxyz"

    while not es_valida:
       letra_elegida = input("Elige una letra:").lower()  # el lower cambia las mayusculas a minusculas
       if letra_elegida in abecedario and len(letra_elegida) == 1:
           es_valida = True
       else:
           print("No has elegido una letra correcta")
    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta)) # pone palabras con espacios


def chequear_letra(letra_elegida , palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has puesto esa letra, intenta otra letra diferente ")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias

def perder():
    print("Ya no te quedan mas vidas")
    print("La palabra correcta es " + palabra)

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("omedeto gozaimasu, has encontrado la palabra !!!")

    return True

palabra,letras_unicas = elegir_palabras(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print("Letras incorrectas:" + '-'.join(letras_incorrectas))
    print(f"vidas:{intentos}")
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos, terminados, aciertos = chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado = terminados





