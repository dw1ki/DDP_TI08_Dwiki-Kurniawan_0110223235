# NO. 1
def profil(nama, alamat, gender, umur, hobi):
    print("Nama:", nama)
    print("Alamat:", alamat)
    print("Gender:", gender)
    print("Umur:", umur, "tahun")
    print("Hobi:", hobi)

profil("Dwiki Kurniawan", "Jalan Gandul No.123", "Laki-laki", 19, "Main Gitar")

#NO.2
def cek_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"
print (cek_kelulusan(60))

# NO.3
def function(nilai):
    if nilai % 2 == 0:
        print("Genap")
    else:
        print("Ganjil")
function(100)