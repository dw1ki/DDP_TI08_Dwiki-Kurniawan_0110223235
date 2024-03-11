# class / template / blue
class Gempa:
    lokasi = "" # class variable
    skala = ""  # boleh ada/tidak

# constructor
    def __init__(self, loc, scale):
        self.lokasi = loc # atribut
        self.skala = scale # atribut

# method
    def dampak(self):
        if self.skala <= 2:
            print("dampak gempa tidak berasa")
        elif self.skala > 2 and self.skala <=4:
            print("dampak gemmpa bangunan retak-retak")
        elif self.skala > 4 and self.skala <= 6:
            print("dampak gempa bangunan roboh")
        else:
            print("dampak gempa bangunan roboh dan berpotensi tsunami")