hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

def lulus_aja(data):
    new_list = []
    
    for item in data:
        if item['nilai'] > 65:
            new_list.append(item['nama'])
    
    return new_list

print(lulus_aja(hasil_akhir))

# no2
fruits = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def reverse(data):
    new_list = []
    
    for item in range(len(data)):
        identity = item + 1
        new_list.append(data[-(identity)])

    return new_list

print(reverse(fruits))

# no3
def duplicate(data):
    new_list = []
    
    for item in data:
        new_list.append(item)
        new_list.append(item)
    
    return new_list

print(duplicate(fruits))

# no4
string = 'nurul fikri'
exclude = ['a', 'i', 'u', 'e', 'o', '']

def konsonan(data):
    new_string = ''
    
    for item in data:
        if item not in exclude:
            new_string += item

    return new_string

print(konsonan(string))