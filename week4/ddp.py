#If Multi Kondisi 1
#deklarasi dan inisialisasi variabel
pelanggan = "budi santoso"
totalBelanja = 150000

#struktur kendali if
if(totalBelanja > 100000) :
    keterangan = "Selamat Anda mendapat hadiah"
else:
    keterangan = "Terima kasih sudah berbelanja"

#cetak data
print("Pelanggan",pelanggan,"\nTotal Belanja Anda Rp.",totalBelanja,"\n",keterangan)

#If Multi Kondisi 2
nama = "Budi Santoso"
nilai = 68.60
# Uji grade dengan IF Multi Kondisi
if (nilai >= 85 and nilai <= 100):
    grade = "A"
elif (nilai >= 75 and nilai < 85):
    grade = "B"
elif (nilai >= 60 and nilai < 75):
    grade = "C"
elif (nilai >= 30 and nilai < 60):
    grade = "D"
else:
    grade = "E"

print(nama, "mendapatkan grade", grade)

