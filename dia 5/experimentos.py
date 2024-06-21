dolares = 1500
euros = dolares * 0.90
def usd_a_eur (dolares):
    return dolares*0.90

print(euros)

# funcion para invertir paralabras y en mayusculas

palabra = " lo que quiera pa "
def invertir_palabras(palabra):
    palabra = palabra[::-1] # invierte las palabras
    palabra = palabra.upper()
    return palabra
print(invertir_palabras(palabra))


lista_numeros = [54,456,589,6985,87,9,87]
def todos_positivos(lista_numeros):
    for num in lista_numeros:
        if num < 0:
            return False
        else:
            pass
    return True
resultado = todos_positivos(lista_numeros)
print(resultado)


# crear una funcion suma menores de una liosta siempre y cuando sean mayores a 0 y menores a 1000 y devolver el resultado

lista_numeros = [5,4,5,45,25,45,26,21,23]
def suma_menores(lista_numeros):
    suma = 0
    for num in lista_numeros:
        if num in range(0,1000):
            suma += num
        else:
            pass
    return suma
resultado = suma_menores(lista_numeros)
print(resultado)



# crear una funcion que cuente la cantidad de pares que existen en la lista y devuelva el resultado


lista_numeros = (4,5,2,3,6,8,45,1,21,22,65,83)
def cantidad_pares(lista_numeros):
    pares = 0
    for num in lista_numeros:
        if num % 2 ==0:
            pares += 1
        else:
            pass
    return pares
resultado = cantidad_pares(lista_numeros)
print(resultado)


