# los sets se pueden declarar con set (1,2,2,) o solo llaves {}
# en los sets no puedo incluir listas ni diccionarios

#mi_set = set([1,2,3,4,5])
#print(type(mi_set))
#print(mi_set)

# otra forma sin palabra set

#print(type(otro_set))
#print(otro_set)

#mi_set = set(1,2,3(5,4,8)) # si puede tener tuplas
#print(type(mi_set))
#print(mi_set)

mi_set = set((1,2,3,4,5))
print(len(mi_set)) # calcula el largo
print(2 in mi_set) # digame si el 2 esta en el set

s1 = {1,2,3}
s2 ={3,4,5}
s3 = s1.union(s2)  # para unir dos sets
print(s3)

s1 = {1,2,3}
s1.add(4) # para agregar  si ponemos un valor que ya esta no lo agrega
s1.remove(2) # para eliminar un valor
s1.discard(3) # descarta los elementos  si pongo un elemento que no existe no da error
s1.pop() # elimina un elemento aleatorio se puede usar en sorteo
s1.clear() # vacia el set 
print(s1)
