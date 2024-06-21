# las funciones recursivas : es una funcion que se llama asi misma a lo largo de ejecucion o intrucciones

def cuenta_atras(numero):
    print(numero)
    numero -= 1
    if numero >0:
        cuenta_atras(numero)
    else:
        print("hola lindo")
    print(f"orden de la liberacion {numero}")
cuenta_atras(10)


def calcular_factorial(numero):
    if numero >1:
        numero = numero * calcular_factorial(numero - 1)
    else:
        numero = 1
    return numero
print(calcular_factorial(0))