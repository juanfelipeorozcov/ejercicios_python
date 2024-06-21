# crear una funcion que devuelva un resultado al lanzar una moneda al azar "cara o cruz"

lista_numeros = [1,25,36,45,14,25,856,85,78]
import random

def lanzar_moneda():
    resultado = random.choice([ "cara", "cruz" ])
    return resultado

def probar_suerte( moneda,lista):
    if moneda == "cara":
        print("La lista se autodestruira")
        return []
    elif moneda == "cruz":
        print("La lista fue salvada")
        return lista

resultado = lanzar_moneda()
lista_resultante = probar_suerte(resultado,lista_numeros)
print("Lista resultante:", lista_resultante)
