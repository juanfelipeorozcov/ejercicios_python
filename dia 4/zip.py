# zip combina dos o mas listas entrelazando los elementos en tuples

nombres = ["juan", "pablo", "ana"]
edades = [25,42,33]
ciudades =["pereira","la_plata","bogota"]


combinados = list(zip(nombres,edades,ciudades)) #llega hasta el largo de la lista mas corta
print(combinados)


for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")



#nombre = ["juan", "sakura","iroshi"]
#edad = [28,28,35]

#combinadis = list(zip(nombre,edad))
#print(combinadis)