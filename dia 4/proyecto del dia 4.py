l
numero
es
menor
a
1
o
superior
a
100(incorrecto)
# si es menor al que escocgio el programa respiuesta incorrecta y decir que escogio un numero menir
# si es mayor que el del programa
# si acierta decir que gano y el numero de intentos    hcarlor hasta que gaste los 8 intentos
# preguntar el nombre al usuario tienes 8 intentos para adivinarlo
# si e

# adivinador de numeros

from random import randint

intentos = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un numero entre el 1 y 100\nTienes 8 intentos")

while intentos < 8:
    estimado = int(input("Cual es el numero?:"))
    intentos += 1

    if estimado < numero_secreto:
        print("Mi numero es mas alto ")

    if estimado > numero_secreto:
        print("Mi numero es mas bajo ")

    if estimado == numero_secreto:
        print(f" Felicitaciones {nombre}! has adivinado en {intentos}")
        break
if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")

# podemos hacer el loops con elif y else tambien debemos definir el estimado antes del loop
 # estimado = 0
 # if estimado not it range (1,101)
     # print("tu numero no se encuentra en el rango")
 # if estimado < numero_secreto:
     # print( "mi numero es mas bajo ")
 # elif estimado > numero_secreto:
     # print( " mi numero es mas alto ")
 # else:
     # print(f" felicitaciones {nombre}! has adivinado en {intentos}")
    #  break
