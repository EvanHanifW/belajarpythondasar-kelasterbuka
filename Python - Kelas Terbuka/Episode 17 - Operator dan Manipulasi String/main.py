# Operator dalam bentuk method


## Mengubah case
# salam.upper() -> uppercase semua
# salam.lower() -> lowercase semua


## Pengecekan isX
# salam.islower() -> apakah lowercase semua
# salam.isupper() -> apakah uppercase semua
# salam.isalpha() -> mengecek apakah semuanya alphabet
# salam.isalnum() -> mengecek apakah alpha numeric
# salam.isdecimal() -> mengecek apakah angka saja
# salam.isspace() -> mengecek apakah spasi (tab, newline, dll)
# salam.istitle() -> apakah awal kata huruf besar?


## startswith() endswith
cek_start = 'Apakah ada'.startswith('Apakah')
print(cek_start)
end_with = 'Apakah ada'.endswith('ada')
print(end_with)


## Penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu'] 
gabungan = 'ya'.join(pisah)
print(gabungan)

gabungan = 'akuyaapayaaku'
print(gabungan.split('ya'))


## alokasi karakter rjust(), ljust(), center()
kanan = 'kanan'.rjust(10, '=')
print("'", kanan, "'")
kiri = 'kiri'.ljust(10, '-')
print("'", kiri, "'")
tengah = 'tengah'.center(10, ';')
print("'", tengah, "'")

# strip()
tengah.strip(';') # menghilangkan tanda ;