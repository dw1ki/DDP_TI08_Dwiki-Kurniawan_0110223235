class Orang:
    def__init__(self, fnama, lnama)
    self.fnama = fnama
    self.lnama = lnama

def jalan(self):
    print("saya bisa jalan")

def cetak(self):
    print("nama saya ",self.fnama, self.lnama)

class Mahasiswa(Orang):

    def__init__(self, fnama, lnama, prodi, angkatan)
    super().__init__(fnama, lnama)
    self.prodi = prodi
    self.angkatan = angkatan

    def print(self):
        super().cetak()
        print("prodi saya ", self.prodi)
        print("saya angkatan ", self.angkatan)

class Karyawan(Orang):
    def__init__(self, fnama, lnama, jabatan)
    super().__init__(fnama, lnama)
    self.jabatan = jabatan

    def tampil(self):
        super().cetak()
        print("jabatan saya ", self.jabatan)

# objek orang
x = Orang("Bagus", "Maulana")
x.cetak()
# x.tampil()

# objek Mahasiswa
y = Mahasiswa("Gilang", "Dirga", "Teknik Informatika", 2023)
y.print()
y.jalan()

# Objek Karyawan
agus = Karyawan("Agus", "Gumilang", "Supervisor")
agus.tampil()
agus.cetak()