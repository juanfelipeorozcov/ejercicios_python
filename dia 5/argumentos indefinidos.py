# **Kwargs palabras claves es una convencion con una condicion de tener dos asteriscos juntos

def suma(**kwargs):
    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total


#print(suma(x=3, y=5, z=2))


def prueba( num1,num2, *args, **kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print( f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [4778,456,4552]
kwargs = {"x":"uno","y":"dos","z":"tres"}

prueba(15,50,45, *args, **kwargs)


