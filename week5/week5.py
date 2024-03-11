#Soal No.1
myList = ["B 125324 ZHE", "Motor", 125, "Abu-Abu"]

print(myList)

#Soal No.2
myList.append(25000000)
myList.append(2)
myList.insert(2,"Vario")
myList.insert(3, "Matic")
print(myList)

#Soal No.3
luas = input("Pilihlah luas (1. Persegi, 2. Lingkaran, 3. Segitiga): ")

match luas:
    case "1"|"Persegi"|"persegi":
        sisi = int(input("Masukan nilai sisi: "))
        luas = sisi*sisi
        print(luas)
    case "2"|"Lingkaran"|"lingkaran":
        jarijari = int(input("Masukan nilai jarijari: "))
        luas = 3.14*jarijari*2
        print(luas)
    case "3"|"Segitiga"|"segitiga":
        alas = int(input("Masukan nilai alas: "))
        tinggi = int(input("Masukan nilai tinggi: "))
        luas = alas*tinggi/2
        print(luas)
    case _:
        print("coba lagi")
