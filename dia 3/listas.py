mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
mi_lista3 = mi_lista + mi_lista2 # sumo las dos listas
resultado = len(mi_lista) # se cuantos elementos tiene la lista
resultado = mi_lista[0:1] # indices que van de 0 a 1
mi_lista3[0] = "alfa"  # puedo sobrescribir cualquier valor de la lista
mi_lista3.append("g") # puedo agregar un elemento a la lista con .append
mi_lista3.pop(0) # elimina cualquier elemento
eliminados = mi_lista.pop(2) # lo elimina y queda guardado en eliminados 
print(mi_lista3)

# otro ejercicios listas desordenadas


lista = ["g","o","b","m","c"]
lista.sort() # organiza la lista
lista.reverse() # lo contrario la desorganiza
print(lista)  #organiza la lista en orden alfabetico



