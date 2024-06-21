# importar metodos a python nos devuelve un numero entero aleatorio

#metos de random
#- randit()
#- uniform()
#- choise()
#- shuffle

from random import randint

aleatorio = randint(1,50)
print(aleatorio)

# uniform : me tira decimales

from random import *

aleatorio = round(uniform(1,5),1) # el reound es para redondear y el uno del final para la can de decimales
print(aleatorio)


aleatorio = random() # siempre va vacio siempre da fraccion de un entero es bueno para porcentajes
print(aleatorio)

# choise

colores = ["rojo","azul","verde"]
aleatorio =  choice(colores)
print(aleatorio)

# shufle # mezcla de forma distinta no se usa con strings

numeros = lista(range(5,50,5))
shuffle(numeros)
print(numeros)
