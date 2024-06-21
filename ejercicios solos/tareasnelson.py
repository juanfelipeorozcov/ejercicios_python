import random

class Animal: #siempre la primera en mayuscula y en singular
    raza: str
    edad: int
    peso: float


    def __init__(self, raza: str, edad: int, peso: float):

        self.raza = raza
        self.edad = edad
        self.peso = peso

    def introduce (self):
        print(f"es un {self.raza}")

    def __str__(self) ->str:
        return (
            "\n___________________\n"
            f"raza = {self.raza}\n"
            f"edad = {self.edad}años\n"
            f"peso = {self.peso} kg\n"
        )

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    perros = Animal(raza ="pastor_aleman",edad=2, peso=28)
    print(perros)
    print(perros.raza)
    perros.introduce()

    gatos = Animal(raza="callejero", edad=8, peso=8)
    print(gatos)
    print(gatos.raza)
    gatos.introduce()

    #users = [animales(name=f"user#{i})", age=random.randint(a:1, b:40), height=random.randrange(start=)]