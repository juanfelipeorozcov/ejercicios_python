 # loops o bucles que se repita
 # for = n veces
 # while = infinitas veces

 # loop for

nombres = ["juan","ana","carlos","belen","fran"] # por cada uno vamos a imprimir hola

for letra in nombres:
    numero_letra = nombres.index(letra) + 1
    print(letra + " hola ")
    print(f"letra {numero_letra}: {letra}")

for nomb in nombres:  # busca cual empieza  por la letra b
    if nomb.startswith("b"):
        print(nomb)
    else:
        print(" nombre que no empieza por b ")

numeros = [ 1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
    print ( mi_valor)


palabra = "python"
for letra in palabra:
    print(letra)


for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
# iterar en diccionario

dic = { "clave1" :"a", "clave2": "b", "clave3": "c"}
for item in dic.items(): # para ver los valores pongo dic.values
    print(item)

# loops con ciclo while: se repite mientras se cumple la condicion
# ejemplo = un jugador muere hasta que el jugador pierda las vidas

#while = mientras que
#else: o se cumple este

monedas = 5
while monedas > 0:
    print(f" Tengo {monedas} monedas")
    monedas = monedas - 1 # (puedo poner tambien monedas -= 1)
else: print(" no tengo mas dinero ")

# ejemplo de while pero para que el usuario pueda manipular el resultado

respuesta = "s"

while respuesta == "s":
    respuesta = input(" quieres seguir? (s/n")
else:
    print("gracias")

# pass = no hacer nada

respuesta = "s"

while respuesta == "s"
    pass   # guarda el lugar

print("a buenbo")

# break = para interrumpir

nombre = input(" tu nnombre")

for letra in nombre:
    if letra == "r"
        break    # continue lo puedo usar tambien aca y es para continuar
    print(letra)

# un loop que reste de uno en uno los numeros condiciones divisble por 5 si no continuar

numero = 50
while numero >= 0
    if numero % 5 == 0:
        print(numero)
        numero = numero -1   # numero -= 1
    else:
        numero = numero -1