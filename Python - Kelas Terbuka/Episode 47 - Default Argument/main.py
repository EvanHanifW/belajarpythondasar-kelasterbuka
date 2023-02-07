''' Default Argument '''

import os

# def fungsi(argument):
# def fungsi(argument = nilai default):
os.system('cls')

# Contoh 1
def say_hello(nama = 'Ganteng'):
    ''' Fungsi dengan default argument'''
    print(f'Halo {nama}')

say_hello('ucup')
say_hello()

# Contoh 2
def sapa_dia(nama, pesan = 'Semoga selalu bahagia'):
    ''' Fungsi dengan 1 input biasa, dan 1 default argument'''
    print(f'Hai {nama}, {pesan}')

sapa_dia('Evan')
sapa_dia('Evan', 'Panjang umur')

# Contoh 3
def hitung_pangkat(angka, pangkat=2):
    return angka ** pangkat

print(hitung_pangkat(2, 4))
print(hitung_pangkat(pangkat=5, angka=2))

# Contoh 4
def fungsi(angka1=1, angka2=2, angka3=3):
    return angka1 + angka2 + angka3

print(fungsi(angka2=3))

