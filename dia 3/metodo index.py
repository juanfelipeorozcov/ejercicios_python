# metodo index o indice los indices en python siempre comienzan en la posición 0

mi_texto = "esta es una prueba"
resultado = mi_texto[0]
print(resultado)
# ahora vamos al reves cual es el caracter y saber en que indice se encuentra

mi_texto = "Esta es una prueba "
resultado = mi_texto.index("n", 5 ) # si busco mayuculas o una letra que no existe va a soltar error
print(resultado)  # si pongo una coma y el indice 5 inicia a nbuscar desde ahi o tambien puedo poner hasta dobde

mi_texto = "Esta es una prueba "
resultado = mi_texto.rindex("a") # con eñ rindes busca de para atras
print(resultado