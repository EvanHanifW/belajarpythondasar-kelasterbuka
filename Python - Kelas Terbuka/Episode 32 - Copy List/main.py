## Teknik menduplikat list


# Teknik duplikat salah
data1 = ['Ucup', 'Evan', 'Otong', 'Dudung', 'Reza']
print(f'Data = {data1}')

data2 = data1 # Duplikat yang salah -> Pass by reference
print(f'Data 2 = {data2}')

# Merubah data 1 -> Akan merubah 2 list 
# karena memiliki address yang sama
data1[0] = 'Bruze'
data2.sort()
print(f'Data = {data1}')
print(f'Data 2 = {data2}')

# Cek adress kedua list
print(f'Address  data1 = {hex(id(data1))}')
print(f'Address  data2 = {hex(id(data2))}')


# Menduplikat list dengan copy (.copy()) -> SOLUSI
print('Membuat list data 3 dengan data1.copy()')
data3 = data1.copy() # Full duplicate

# Cek address ketiga list
print(f'Address  data1 = {hex(id(data1))}')
print(f'Address  data2 = {hex(id(data2))}')
print(f'Address  data3 = {hex(id(data3))}')

print(f'Data 1 = {data1}')
print(f'Data 2 = {data2}')
print(f'Data 3 = {data3}')

print('Merubah data data3[1]')
data3[1] = 'Pekel'

print(f'Data 1 = {data1}')
print(f'Data 2 = {data2}')
print(f'Data 3 = {data3}')