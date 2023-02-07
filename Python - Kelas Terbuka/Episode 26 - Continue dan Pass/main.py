# continue, pass, break


# pass -> berfungsi sebagai dummy, tidak dieksekusi
angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass
    print(angka)


# continue
angka = 0
print(f'Angka saat ini -> {angka}')

while angka < 5:
    angka += 1
    print(f'Angka sekarang -> {angka}')

    if angka == 3:
        print('Nice!')
        continue # lanjut ke step selanjutnya
    print('Whassap')
print('Nice!')