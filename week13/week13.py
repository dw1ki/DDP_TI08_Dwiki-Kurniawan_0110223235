class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

class Serigala(Animal):
    def __init__(self, name, food, habitat, reproduction):
        super().__init__(name, food, habitat, reproduction)
        
    def Serigala(self):
        print(f'Nama \t: {self.name} \nMakanan : {self.food} \nHabitat\t : {self.habitat} \nBerkembangbiak\t : {self.reproduction}')

class Chicken(Animal):
    def __init__(self, name, food, habitat, reproduction):
        super().__init__(name, food, habitat, reproduction)
        
    def Ayam(self):
        print(f'Nama \t: {self.name} \nMakanan : {self.food} \nHabitat\t : {self.habitat} \nBerkembangbiak\t : {self.reproduction}')

class Shark(Animal):
    def __init__(self, name, food, habitat, reproduction):
        super().__init__(name, food, habitat, reproduction)
        
    def hiu(self):
        print(f'Nama \t: {self.name} \nMakanan : {self.food} \nHabitat\t : {self.habitat} \nBerkembangbiak\t : {self.reproduction}')


serigala = Serigala("Serigala", "Rusa", "Hutan", "Vivipar")
chicken = Chicken("Ayam", "Biji-bijian", "Kebun", "Ovipar")
shark = Shark("Hiu", "Ikan", "Laut", "Vivipar")

serigala.Serigala()
chicken.Ayam()
shark.hiu()
