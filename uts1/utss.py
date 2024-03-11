# Input
panjang = float(input("Masukkan panjang:"))
lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi (h): "))
d1 = float(input("Masukkan diagonal 1: "))
d2 = float(input("Masukkan diagonal 2: "))
nim = int(input("Masukkan NIM: "))

# Proses
if nim % 2 == 1:  # NIM ganjil
    luas = 0.5 * d1 * d2
    keliling = 2 * (panjang + lebar)
    jenis_bangun = "Layang-Layang"
else:  # NIM genap
    luas = 0.5 * (panjang + lebar) * tinggi
    keliling = panjang + lebar + 2 * tinggi
    jenis_bangun = "Trapesium"

# Output
print(f"\nJenis bangun: {jenis_bangun}")
print(f"Luas: {luas}")
print(f"Keliling: {keliling}")