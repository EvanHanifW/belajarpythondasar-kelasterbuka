sisi = 10


# 1. Menggunakan for

# dummy var
print('Awal for')
count = 1
for i in range(sisi):
    print('*' * count)
    count += 1

print('Akhir dari For')


# 2. Menggunakan While
# Segitiga ganjil saja
print('Awal while')
count = 1
spasi = int(sisi/2)

while count < sisi:

    if (count%2): # Kalo ganjil bakal ngeprint bintang
        print(' '*spasi , '*'*count)

        spasi -= 1
        count += 1
        continue # ~count mod 2 akan true jika genap
    else:
        count += 1

print('Akhir while')