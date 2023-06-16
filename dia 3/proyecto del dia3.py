# hacer un codigo analisador de texto
# pida la usuario qaue ingrese un texto
# pedir tres letras a su eleccion
# 1 cuantas veces aparece cada una de las letras (alamacenar en una lista)
# 2 cuantas palabras hay en todo el texto  (transformar el string en una lista)
# 3 primera letra del texto y ultima
# 4 invertir el orden de las palabras
# decir si la palabra python esta dentro del texto

# analisador de texto
texto = input("por favor digite un texto: ")
letras = []
texto = texto.lower() # vuelve todo el texto en minusculas
letras.append(input("ingrese la primera letra: ").lower())
letras.append(input("ingrese la segunda letra: ").lower())
letras.append(input("ingrese la tercera letra: ").lower())

print("\n")    # alt + 92 barra invertida
print("CANTIDAD DE LETRZAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2= texto.count(letras[1])
cantidad_letras3= texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidad_letras3} veces")

# poner cantidad de palabras

print("\n") # salto de linea
print("CANTIDAD DE PALABRAS")
palabras = texto.split()  # separa el texto en porciones crea una lista
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

# indicar letras inicio y fin

print("\n")
print("LETRAS DE INICIO Y DE FIN ")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")
# invertir el texto
print("\n")
print("INVERTIR EL TEXTO")
palabras.reverse()
texto_invertido = " " .join(palabras)
print(f"Si ordenamos tu texto al reves va a decir: '{texto_invertido}'")

# buscar palabra python
print("\n")
print("BUSCAR LA PALABRA PYTHON ")
bucar_python = 'python' in texto
dic ={True: "si", False: "no"}
print(f"La palabra python {dic[bucar_python]} se encuentra en el texto")


print(texto)
print(letras)





