# Break

data_int = int(input('Hitung sampai = '))
angka = 0

while True:
    angka += 1
    print(f'Count = {angka}')
    
    if angka == data_int:
        print('Nice!')
        break

    print('wasap')
print('Finish')