diccionario = {"c1": "valor1" , "c2": "valor2"} # los valores se pueden repetir, pero las claves no se pueden repetir

print(diccionario)
resultado = diccionario["c1"]
print(resultado)

cliente = {"nombre": "juan", "apellido":"orozco","peso":60,"talla":1.72}
consulta = (cliente["apellido"])   # como pedi el apellido me miuestra solo el apellido
print(consulta)

dic = {"c1":55,"c2":[10,20,30],"c3":{"s1":100},"s2":200}
print(dic["c2"][1]) # me busca en c2 que es una lista el 1 que es el 20 dentro de la lista me busca el valor que quiero

dic = {"c1":["a","b","c"], "c2":["d","e","f"]}
print(dic["c2"][1].upper()) # en una sola linea imprimir la letra E en mayusculas

dic = {1:"a",2:"b"}
print(dic)
dic[3] = "c"   # agregue c al diccionario
print(dic)
dic[2] = "8"  # cambie b por el numero 8
print(dic)

print(dic.keys()) # trae todas las llaves que tiene
print(dic.values()) # valores
print(dic.items()) # todos los elementos en el diccionario