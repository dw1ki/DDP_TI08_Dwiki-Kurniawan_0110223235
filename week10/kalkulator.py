import math

def tambah(a, b): 
    hasil = a + b
    return f'memiliki hasil pertambahan: {hasil}'

def kurang(a, b):
    hasil = a - b
    return f'memiliki hasil pengurangan: {hasil}'

def pangkat(a, b):
    hasil = a ** b
    return f'memiliki hasil perpangkatan: {hasil}'

def kali(a, b):
    hasil = a * b
    return f'memiliki hasil perkalian: {hasil}'

def bagi(a, b):
    hasil = a / b
    return f'memiliki hasil pembagian: {hasil}'

def log(a: int):
    return f'hasil {math.log(a)}'

def akar(a: int):
    return f'hasil {math.sqrt(a)}'

def sin(a: int):
    return f'hasil {math.sin(a)}'

def cos(a: int):
    return f'hasil {math.cos(a)}'

def tan(a: int): 
    return f'hasil {math.tan(a)}'