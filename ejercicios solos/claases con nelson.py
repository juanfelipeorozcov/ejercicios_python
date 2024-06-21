import random


class person:
    name: str
    age: int
    height: float

# necesitamos el constructor (es un para crear el objeto)

    def __init__(self, name: str, age: int, height: float): # self siempre debe ir primero con este accede a los atributos y metodos
        self.name = name
        self.age = age
        self.height = height



if __name__ == "__main__":
    lulo = person(name="lulo",age=45, height=140)
    print(lulo)
    print(lulo.name)
    lulo.introduce()

    juan = person(name="juan", age=18, height=190)
    print(juan)
    print(juan.name)
    juan.introduce()

    users = [person(name=f"user#{i})", age=random.randint(a:1, b:40), height=random.randrange(start=)]