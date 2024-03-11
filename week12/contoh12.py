class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

class Rhino(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, "Tumbuhan", habitat, "Vivipar")

    def charge(self):
        print(f"{self.name} sedang menyerang!")

class Fish(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, "Plankton", habitat, "Ovipar")

    def swim(self):
        print(f"{self.name} sedang berenang!")

class Snake(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, "Hewan Kecil", habitat, "Ovipar")

    def slither(self):
        print(f"{self.name} sedang merayap!")

# Contoh penggunaan
rhino = Rhino("Badak Sumatera", "Hutan")
rhino.charge()

fish = Fish("Ikan Koi", "Kolam")
fish.swim()

snake = Snake("Ular Sanca", "Hutan")
snake.slither()
