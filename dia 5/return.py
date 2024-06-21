# si usamos el return nos devuelve un resultado no solo queda escrito

def multiplicar(num1,num2):
    return num1 * num2       # el resturn queda guardado para usarlo en futuras operaciones
resultado = multiplicar(5,10)
print(resultado)

# otra forma
def multiplicar(num1,num2):
    total = num1 * num2
    return total
resultado = multiplicar(5,10)
print(resultado)

# ejercicios de return
''' Crea una función llamada potencia que tome dos valores numéricos como argumentos.
 Deberá devolver el número que resulte de resolver una potencia,
  utilizando el primer número como base, y el segundo como exponente:
'''
def potencia(num1,num2):
    return num1**2num2


