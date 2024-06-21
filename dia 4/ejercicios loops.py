lista_numeros = [1,5,6,8,5,6,5]
suma_numeros = 0
for resultado in lista_numeros:
    suma_numeros = suma_numeros + resultado
    print(suma_numeros)

# para sumar pares e impares en diferentes lados
lista_numeros = [1,5,7,9,8,5,6,5,7,8,4,5,2,6,8]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares =suma_pares + numero
    else:
        suma_impares = suma_impares + numero



# ejercicio de enumerador imprimir en pantalla los nombres de la lista  que solo
# comiencen con la letra M

lista_nombres = ["pablo","roberto","mauricio","murillo"]
  for lista, nombre in enumerate(lista_nombres):
      if nombre [0] == "m":
       print(lista)