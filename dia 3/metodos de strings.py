# upper() sirve para pasar a mayusculas
# lower() sirve para minusculas
# split () separar en partes (listas)
#join() unir items usando separador
# find () encontrar un sub-string
# replace () reemplazae un substring


texto = "este es el texto de juan "


resultado = texto[2].upper() # lo pone en may // si le pongo [2] solo la casilla dos se vuelve may
resultado = texto.split() # para separar las listas 
resultado = texto.find("s")
resultado = texto.replace("juan","todos ")
print(resultado)


# metodo join
a = "aprender"
b = "python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)