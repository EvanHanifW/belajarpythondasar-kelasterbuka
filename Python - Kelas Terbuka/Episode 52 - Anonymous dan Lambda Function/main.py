# lambda function

def kuadrat(angka):
    return angka ** 2

print(f'Hasil dari fungsi kuadrat{kuadrat(9)}')


# coba implementasi lambda
# output = lambda argument: expression
fungsi_kuadrat = lambda angka: angka ** 2
print(f'Hasil dari fungsi lambda {fungsi_kuadrat(5)}')

pangkat = lambda num, pow: num ** pow
print(f'Hasil dari lambda pangkat {pangkat(4,2)}')


## kegunaan

# sorting list biasa
data_list = ['evan', 'ucup', 'otong']
data_list.sort()
print(f'Sorted list = {data_list}')

# sorting pakai panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f'Sorted list by panjang= {data_list}')

# sort pake lambda
data_list.sort(key=lambda nama: len(nama))
print(f'Sorted list by panjang= {data_list}')


# filter
data_angka = [1,21,3132,231,31,23,121,3]
def kurang_dari_lima(angka):
    return angka < 5
data_angka_baru = list(filter(lambda x: x<5, data_angka))

print(data_angka_baru)


# kasus genap
data_genap = list(filter(lambda x:(x%2 == 0), data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x:(x%2 != 0), data_angka))
print(data_ganjil)

# kelipatan 3
data_kelipatan3 = list(filter(lambda x:(x%3 == 0), data_angka))
print(data_kelipatan3)


# anonymous function
# currying <- Haskell Curry

def pangkat(angka, n):
    return angka ** n

print(f'Fungsi biasa = {pangkat(5, 3)}')

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f'pangka2 = {pangkat2(5)}')
print(f'pangka bebas = {pangkat(4)(5)}')