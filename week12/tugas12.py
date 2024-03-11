class binatang:

    def __init__(self, fname, makanan, hidup, berkembangbiak):
        self.name = fname 
        self.makanan = makanan
        self.hidup = hidup
        self.biak = berkembangbiak

class harimau(binatang):
    def __init__(self, fname, makanan, hidup, berkembangbiak):
        super().__init__(fname, makanan, hidup, berkembangbiak)

    def maung(self):
        print(f'Nama \t:  {self.name}  \nMakanan :  {self.makanan} \nhidup  \: {self.hidup} \nBerkembangbiak \t: {sel

class sapi(binatang):
    