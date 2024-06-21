import random


def lanzar_dados() -> tuple[int, ...]:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2


def evaluar_jugada(dado1: int, dado2: int):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable "
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


# lanzar los dados
resultado_dado1, resultado_dado2 = lanzar_dados()
# evaluar la jugada
mensaje = evaluar_jugada(resultado_dado1, resultado_dado2)
print(mensaje)

