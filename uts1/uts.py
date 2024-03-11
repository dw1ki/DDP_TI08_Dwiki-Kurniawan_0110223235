def kalkulator_sederhana():
    
    angka1 = float(input("Masukkan angka 1: "))
    angka2 = float(input("Masukkan angka 2: "))
    
    
    print("Pilih operator:")
    print("+ : Tambah")
    print("- : Kurang")
    print("/ : Bagi")
    print("* : Kali")
    print("** : Pangkat")
    
    operator = input("Pilihan Operator: ")


    if operator == '+':
        hasil = angka1 + angka2
    elif operator =='-':
        hasil = angka1 - angka2
    elif operator == '/':
        hasil = angka1 / angka2
    elif operator == '*':
        hasil = angka1 * angka2
    elif operator == '**':
        hasil = angka1 ** angka2
    else:
        print("Operator tidak valid.")
        return
    
    
    print(f"Angka pertama: {angka1}")
    print(f"Angka kedua: {angka2}")
    print(f"Pilihan Operator: {operator}")
    print(f"Hasil operator {angka1} {operator} {angka2} = {hasil}")

kalkulator_sederhana
kalkulator_sederhana()