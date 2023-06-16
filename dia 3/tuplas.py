# son iguales a las listas pero son inmutables no llevan corchetes si no parentesis
# ocupan menos espacio en memoria y son mas rapido que las listas y se usan cuando no quiero modificar algo
 # no se puede cambiar pero si podemos anidar

mi_tuple = (1,2,(10,20),4)
mi_tuple = list(mi_tuple) # guardar en una lista
print(type(mi_tuple))

t = (1,2,3,1) # para darle estos valores a x,y,z siempre tienen que tener los mismos valores
x,y,z = t
print(x,y,z)

print(t.count(1)) # cuento cuantas veces esta el 1
print(t.index(2)) # valor sobre el cual quiero consultar su indice

# convertir a lista la siguiente tupla y almacenala en una variable llamada mi_lista

mi_tupla = (1,2,3,2,3,1,3,2)
mi_lista = list(mi_tupla)
print(mi_lista)