import random


def dividir (a: int, b: int) -> int:
    try:
        return a // b
    except zeroDivisionError:
        return 0

def error_random()  # error de forma aleatoria
    if random.choice([True, False]):
        raise Exception ("Falle")

def retry(my_func: callable,n_retries: int) -> callable:

    def my_internel(*args, **kwargs, ):
        try:
            my_func(*args, **kwargs)
        except Exception:

    return my_internel()




if __name__ == "__main__":
    result = dividir(a: 5, b: 2)
    print(result)
    result = dividir(a: 5, b:3)
    print(result)

    error = False

    while not error:
        try:
            error_random()
        except Exception:
            error = True