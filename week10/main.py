import bangundatar, kalkulator
from bangundatar import *
from kalkulator import *

# segitiga
tinggi = int(input('masukkan tinggi: '))
alas = int(input('masukkan alas: '))
sisi1 = int(input('masukkan sisi1: '))
sisi2 = int(input('masukkan sisi2: ')) 
sisi3 = int(input('masukkan sisi3: '))
print(segitiga(alas, tinggi,sisi1, sisi2, sisi3))

# persegi
sisi = int(input('masukkan sisi: '))
print(persegi(sisi))

# persegi panjang
panjang = int(input('masukkan panjang: '))
lebar = int(input('masukkan lebar: '))
print(persegi_panjang(panjang, lebar))

# belah ketupat
diagonal1 = int(input('masukkan diagonal 1: '))
diagonal2 = int(input('masukkan diagonal 2: '))
sisi = int(input('masukkan sisi: '))
print(belah_ketupat(diagonal1, diagonal2, sisi))

# jajar genjang
alas = int(input('masukkan alas: '))
tinggi = int(input('masukkan tinggi: '))
sisi_miring = int(input('masukkan sisi miring: '))
print(jajar_genjang(alas, tinggi, sisi_miring))

# pertambahan
a = int(input('masukkan nilai pertama: '))
b = int(input('masukkan nilai kedua: '))
print(tambah(a, b))

# pengurangan
a = int(input('masukkan nilai pertama: '))
b = int(input('masukkan nilai kedua: '))
print(kurang(a, b))

# perpangkatan
a = int(input('masukkan nilai pertama: '))
b = int(input('masukkan nilai kedua: '))
print(pangkat(a, b))

# perkalian
a = int(input('masukkan nilai pertama: '))
b = int(input('masukkan nilai kedua: '))
print(kali(a, b))

# pembagian
a = int(input('masukkan nilai pertama: '))
b = int(input('masukkan nilai kedua: '))
print(bagi(a, b))

# log
print ('log')
a = int(input('masukkan nilai: '))
print(kalkulator.log(a))

# akar
print ('sqrt')
a = int(input('masukkan nilai: '))
print(kalkulator.akar(a))

# sin
print ('sin')
a = int(input('masukkan nilai: '))
print(kalkulator.sin(a))

# cos
print ('cos')
a = int(input('masukkan nilai: '))
print(kalkulator.cos(a))

# tan
print ('tan')
a = int(input('masukkan nilai: '))
print(kalkulator.tan(a))