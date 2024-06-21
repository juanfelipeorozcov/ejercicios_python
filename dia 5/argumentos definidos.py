# *args podemos definir funciones cuyos numeros de argumentos sean variables ( numero de parametro variables)

#def suma (a,b):
 #   return a+b
#print(suma(5,6,4))


# ahora con el * arg

def suma(*args):   # puedo cambiar el args por cualquier nombre aviones, carros,elefantes
    total = 0

    for arg in args:
        total += arg
    return total

print(suma(5,5,8,6,4,7,8,5,8,58,54785)) # puedo colocar los valores que qauiera

# una forma de hacerlo mas simple

def suma(*args):

    return sum(args)

print(suma(4,5,4,5,8,5,6,4,5,65,585,7,8))



# abs es para el valor absoluto suma positivos y negativos


# ejercicio crear una funcion que revciba un combre y una cantidad de números indefinida y que devuelva el mensakje


def  numeros_persona(nombre,*args):
    suma_numeros = sum(args)
    return f"{nombre}, La suma de tus numeros es {suma_numeros}"
nombre = "juan"
resultado = numeros_persona(nombre, 10 58,54,47)

print(resultado)