def segitiga(tinggi, alas, sisi1, sisi2, sisi3):
    keliling = sisi1 + sisi2 + sisi3
    luas = (tinggi * alas) * 0.5
    return f'luas segitiga adalah {luas}, dan keliling segitiga adalah {keliling}'

def persegi(sisi):
    keliling = 4 * sisi
    luas = sisi * sisi
    return f'luas persegi adalah {luas}, dan keliling persegi adalah {keliling}'

def persegi_panjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar
    return f'luas persegi panjang adalah {luas}, dan keliling persegi panjang adalah {keliling}'

def belah_ketupat(diagonal1, diagonal2, sisi):
    keliling = 4 * sisi
    luas = 0.5 * (diagonal1 * diagonal2)
    return f'luas belah ketupat adalah {luas}, dan keliling belah ketupat adalah {keliling}'

def jajar_genjang(alas, tinggi, sisi_miring):
    keliling = 2 * (alas + sisi_miring)
    luas = alas * tinggi
    return f'luas jajar genjang adalah {luas}, dan keliling jajar genjang adalah {keliling}'