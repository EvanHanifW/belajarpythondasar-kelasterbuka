''' Latihan Fungsi '''

import os

# program untuk menghitung luas dan keliling persegi panjang

# membuat header program

def header():
    ''' Fungsi header'''
    os.system('cls')
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    ''' Fungsi input user '''
    lebar = int(input('Masukan lebar : '))
    panjang = int(input('Masukan panjang : '))

    return lebar, panjang

def hitung_luas(lebar, panjang):
    ''' Fungsi hitung luas '''
    return lebar * panjang

def hitung_keliling(lebar, panjang):
    ''' Fungsi keliling '''
    return 2 * (lebar + panjang)

def display(message, value):
    ''' Display function '''
    print(f'Hasil perhitungan {message} = {value}')

while True:
    header()
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display('Luas', LUAS)
    display('Keliling', KELILING)

    isContinue = input('Apakah ingin lanjut? (y/n)')
    if isContinue == 'n':
        break

