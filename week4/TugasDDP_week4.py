# Soal No.1
nama = "Budi Santoso"
usia = 65

if (usia < 18):
    kategori = "anak-anak"
elif (usia >=18 and usia <= 65):
    kategori = "dewasa"
else:
    kategori = "lanjut usia"

print(nama, "adalah kategori", kategori)


#Soal No.2
A = 13
B = 8

if A > B: print(A, "lebih besar dari", B)
elif B > A: print(B, "lebih besar dari", A)
else: print("Angka sama besar")