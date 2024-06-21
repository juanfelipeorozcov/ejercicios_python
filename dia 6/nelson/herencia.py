class Animal:
    kind: str
    height: float
    legs: int
    sound: str

    def __init__(self, kind: str, height: float, legs: int):
        self.kind = kind
        self.height = height
        self.legs = legs
        self.sound

    def make_a_sound(self):
        print("mew")


if __name__ "__main__":
