 # def = (definicion de funcion ):  siempre escribir explicacion con tres comillas simples para decir que hace la funcion

def saludar_persona(nombre):
    #print("hola " + nombre)

saludar_persona("felipe") # aqui llamo la funcion que esta en def
saludar_persona("javier")

# ejercicio:
''' declarar una funcion llamada bienvenida que tome como argumento el nombre de la persona, y que cada vez 
    que sea llamada imprima en pantalla (bienvenido {nombre_persona}! crear una variable nombre_ persona '''

nombre_persona = ("felipe")
def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")
print(nombre_persona)

'''Declara una función llamada cuadrado, que tome como argumento un número cualquiera,
 y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número 
 (es decir, la potencia 2 del valor).
El nombre del argumento que debe tomar dicha función es un_numero.
 Crea dicha variable y asígnale un número cualquiera.
'''
un_numero = 5
def cuadrado(un_numero):
    print(un_numero**2)
# funcion para convertir dolares a euros

dolares = 1500
def usd_a_eur (dolares):
    return dolares*0.90
print()



