# ejercicio 1

# crear una funcion llamada devolver_distintos() que reciba 3 integers como parametros
# si la suma de los 3 numeros es mayor a 15, va a decolver el numero mayor
# si la suma de los 3 numeros es menor a 10 va a devolver el numero menor
# si la suma de los 3 numeros es un valor entre 10 y 15 (incluidos) va a devolver el numero de valor intermedio


def devolver_distintos(a,b,c):

    suma = a+b+c
    lista = [a,b,c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()  # organiza los elementos de la lista
        return lista[1]

print(devolver_distintos(20,52,45,))



 ejercicio 2

 #escribir una funcion con el nombre que quiera, que reciba cualquier palabra como parametro y que devuelva
#todas sus letras unicas sin repetir, pero en orden alfabetico


def letras_unicas(palabre):

    mi_set = set() # asi se pone un set vacio esto deja los elementos unicos no los repite

   for letra in palabre:
        mi_set.add(letra)
     vamos a castearlo dentro de una lista
    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista
print(letras_unicas("cascarrabias"))


 ejercicio 3

# escribe una funcion que requiera una cantidad indefinida de argumentos. lo que hará esta función es devolver True si
# en algun momento se ha ingresado al numero cero repetido dos veces consecutivas.
# por ejemplo (5,6,1,0,0,9,3,5)>>> True     (,6,0,5,1,0,3,0,1)>>> False

def ceros_vecinos(*args):

    contador = 0

    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1 ] == 0:
            return True
        else:
            contador += 1

    return False

print(ceros_vecinos(5,6,5,8,5,8,9,8,5,2,2,1,45,0,0)) # si los dos ceros son vecinos me da true si no hay ceros false


 ejercicio 4

# Escribe una función llamada contar_primos() que requiera un solo argumento numérico
# Esta función va a mostrar en pantalla cuántos números primos hay en el rango que va desde cero hasta ese número
#incluido, y va a devolver la cantidad de números primos que encontró

def contar_primos(numero):

    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:
        for n in range(3,iteracion,2):

            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion) # append agrega cosas
            iteracion += 2

    print(primos)
    return len(primos) # retorna el largo de la lista

print(contar_primos(50))















# escriba una funcion llamada contar_primos() que requiera un solo argumento numerico
# esta funcion va a mostrar en pantalla todos los numeros primos existentes en el rango que va desdde cero hasta
# es numero incluido y ya devolver la cantidad de numeros primos que en encontro

