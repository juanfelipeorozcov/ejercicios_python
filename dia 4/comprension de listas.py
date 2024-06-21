# forma facil de crear listas

palabra = "phyton"

lista = []

for letra in palabra
    lista.append(letra)
print(lista)

# si lo quiero de hacer de una forma mas facil

palabra = "phyton"

lista = [letra for letra in palabra]

print(lista)

lista =[n for n in range (0,21,2)] # numeros pares de 0 hasta 20 y va de 2 en 2
print(lista)

lista = [ n / 2 for n in range ( 0,21,2)] # mi lista cada numero divido por numero que hay en el rango
print (lista)

lista = [n for n in range (0,21,2) if n * 2>10] # incorporar numeros por cada numero en el rango siemopre y cuando el numero multiplicado por 2 sea mayor
  # a 10

lista =[n if n * 2 > 10 else " no "for n in range (0,21,2)] # incorporar n siempre y cuando n sea mayor de 10 si no pone un  no


pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)


