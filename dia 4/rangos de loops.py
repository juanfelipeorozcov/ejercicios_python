lista = [1,2,3,4]

for numero in lista:
    print(numero)   # forma normal

# lo haremos mas facil colocando parametros con range

for numero in range (5): # lo toma desde el 0  range no recibe floats
    print(numero)
for numero in range (5,20):
    print(numero)

lista = list(range(1,101)) # caso fuera de loops del 1 hasta el 100
      print(lista)


# enumeradores

lista =["a","b","c"]

for indice,item in enumerate(lista): # tambien puede ser con rangos range(5,500))
    print(indice,item)

# lista de tabples  tener acceso a los enumerables
lista = ["a","b","c"]
mis_tuples = list(enumerate(lista))
print(mis_tuples[1][0])