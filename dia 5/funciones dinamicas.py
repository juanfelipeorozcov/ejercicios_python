def chequear_3_cifras(numero):
    return numero in range(100,1000)

suma = 586 + 483 # tambien podemos pasar variables

resultado = chequear_3_cifras( suma )
print(resultado)

# vamos a hacerlo verificando todos los elementos de una lista chequeando si tienene 3 cifras

def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras([555,99,600])
print(resultado)


# crear una lista con numero + y - y decir si con negativos false o positivos true

lista_numeros = [54,456,-589,6985,-87,9,-87]
def todos_positivos(lista_numeros):
    for num in lista_numeros:
        if num < 0:
            return False
        else:
            pass
    return True
resultado = todos_positivos(lista_numeros)
print(lista_numeros)
