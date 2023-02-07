print(10*'=')
print('Kalkulator sederhana')
print(10*'=')

input1 = float(input('Masukan angka pertama : '))
operator = input('Masukan operator (+, -, /, *)')
input2 = float(input('Masukan angka kedua : '))

if operator == '+':
    hasil = input1 + input2
elif operator == '-':
    hasil = input1 - input2
elif operator == '*':
    hasil = input1 * input2
elif operator == '/':
    hasil = input1 / input2
else:
    print('Masukin operator yang bener dong')
print(f'Hasilnya adalah {hasil}')