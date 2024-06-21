import random

class Vehiculo:
    marca:str
    modelo:int
    color:str

    def __init__(self, marca: str, modelo: int, color: str):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def informacion(self):
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        print(f"color: {self.color}")

class Carro(Vehiculo):
    def __init__(self, marca, modelo, color, puertas):
        super().__init__(marca, modelo, color)
        self.puertas = puertas


    def informacion(self):
        super().informacion()
        print(f"puertas: {self.puertas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, tipo):
        super().__init__(marca, modelo, color)
        self.tipo = tipo

    def informacion(self):
        super().informacion()
        print(f"tipo: {self.tipo}")



carro = Carro("toyota", 2015, "blanco", 4)
carro.informacion()
moto = Moto ("kawazaki", 2015, "verde", "cross")
moto.informacion()

