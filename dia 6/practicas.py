
# ejercicio 1

# crear una funcion llamada devolver_distintos() que reciba 3 integers como parametros
# si la suma de los 3 numeros es mayor a 15, va a decolver el numero mayor
# si la suma de los 3 numeros es menor a 10 va a devolver el numero menor
# si la suma de los 3 numeros es un valor entre 10 y 15 (incluidos) va a devolver el numero de valor intermedio


#def devolver_distintos(a,b,c):

 #   suma = a+b+c
  #  lista = [a,b,c]

   # if suma > 15:
       # return max(lista)

   # elif suma < 10:
    #    return min(lsita)

   # else:
    #    lista.sort() # organiza los elementos de la lista
    #    return lista[1]

#print(devolver_distintos(82,35,67))



# ejercicio #2

# escribe una funcion que requiera una cantidad indefinida de argumentos. lo que hara esta funcion
# En algun momento se ha ingresando al numero cero repetido dos veces consecutivas
# por ejemplo (5,6,1,0,0,9,3,5)>>> True    (6,8,5,1,0,3,0,1)>>> false


def ceros(*args)

    contador = 0

    for num in args:
        if contador + 1 ==
