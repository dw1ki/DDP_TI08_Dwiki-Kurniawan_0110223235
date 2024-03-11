#Soal Nomor 1
bensin = {
    "Pertalite": {"harga": 10000, "jarak": 12},
    "Pertamax": {"harga": 14000, "jarak": 13},
    "Pertamax Turbo": {"harga": 17000, "jarak": 13.5}
}

jarak_kota = {
    "Jakarta": 20,
    "Bekasi": 35.7,
    "Depok": 5,
    "Tangerang": 99,
    "Bogor": 120.6
}

nama_kendaraan = input("Nama Kendaraan(Motor, Mobil): ")
jenis_bensin = input("Jenis Bensin (Pertalite, Pertamax, Pertamax Turbo):")
kota_tujuan = input("Kota Tujuan (Jakarta, Bekasi, Depok, Tangerang, Bogor): ")

if kota_tujuan in jarak_kota:
    jarak_tempuh = jarak_kota[kota_tujuan]
else:
    jarak_tempuh = 0

if jenis_bensin in bensin:
    pemakaian_bensin = jarak_tempuh / bensin[jenis_bensin]["jarak"]
else:
    pemakaian_bensin = 0

total_harga = pemakaian_bensin * bensin[jenis_bensin]["harga"]

print("Nama Kendaraan:", nama_kendaraan)
print("Jenis Bensin:", jenis_bensin)
print("Kota Tujuan:", kota_tujuan)
print("Pemakaian Bensin:", pemakaian_bensin, "liter")
print("Total Harga Bensin:", total_harga, "rupiah")

# Soal Nomor 2
menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Geprek": 18000
}

menu_minuman = {
    "Aneka Jus": 15000,
    "Soft Drink": 10000,
    "Sweet Ice Tea": 5000
}

nama_pembeli = input("Masukkan Nama Pembeli: ")
no_hp_pembeli = input("Masukkan No Hp Pembeli: ")
pesan_menu = input("Pesan Menu (makanan/minuman): ")

if pesan_menu.lower() == "makanan":
    print("Menu Minuman:")
    for minuman, harga in menu_minuman.items():
        print(f"{minuman} - Rp. {harga}")
else:
    print("Menu Makanan:")
    for makanan, harga in menu_makanan.items():
        print(f"{makanan} - Rp. {harga}")

pesanan = input("Masukkan Pesanan: ")
jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

if pesan_menu.lower() == "makanan" and pesanan in menu_makanan:
    harga_total = menu_makanan[pesanan] * jumlah_pesanan
elif pesan_menu.lower() == "minuman" and pesanan in menu_minuman:
    harga_total = menu_minuman[pesanan] * jumlah_pesanan
else:
    harga_total = 0

print("Nama Pembeli:", nama_pembeli)
print("No Hp Pembeli:", no_hp_pembeli)
print("Menu yang dipesan:", pesanan)
print("Jumlah Pesanan:", jumlah_pesanan)
print("Harga yang harus dibayarkan:", harga_total)

# Soal Nomor 3
for i in range(1, 21):
    if i % 3 == 0:
        print("STT Nurul Fikri")
    else:
        print(i)