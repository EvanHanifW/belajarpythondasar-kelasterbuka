## Glocal dan Local scope

nama_global = 'otong' # global variable

# akses global var dalam fungsi
def fungsi(nama):
    print(f'fungsi menampilkan {nama}')

fungsi(nama_global)

# akses global var dalam loop
for i in range(5):
    print(f'loop {i} - {nama_global}')

# percabangan
if True:
    print(f'menampilkan nama global {nama_global}')


## Variable local scope
def fungsi2():
    nama_lokal = 'ucup' # variable local

fungsi2()
# print(nama_lokal) tidak bisa dilakukan 
# karena nama lokal adalah variabel lokal


## contoh 1: penggunaan akses variabel
def say_otong(nama):
    print(f'Hello {nama}')

nama = 'otong'
say_otong(nama) # di pyhton tidak eror karena interpreted


## contoh 2: merubah variabel global
angka = 0

def ubah_angka(nilai_baru):
    global angka # fungsi ini mendapat akses untuk angka global
    angka = nilai_baru

print(f'Angka sebelum = {angka}')
ubah_angka(12)
print(f'Angka sesudah = {angka}')


## contoh 3:
angka = 0

for i in range(5):
    angka += 1
    angka_dummy = 0
print(angka)
print(angka_dummy)

if True:
    angka_dummy = 10
print(angka)
print(angka_dummy)