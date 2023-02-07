data_angka = [1,1,2,41,3,2,3,51,53,6,1,2,3,3,3,2,2,7,8,5]
print(f'Data angka = {data_angka}')


# count data (.count())

jumlah_data_1 = data_angka.count(1)
jumlah_data_3 = data_angka.count(3)
print(f'Jumlah angka 1 = {jumlah_data_1}')
print(f'Jumlah angka 3 = {jumlah_data_3}')

# Ambil posisi data -> cari index (.index())

data = ['Ucup', 'Dudung', 'Ujang', 'Evan']
print(f'Data = {data}')
index_dudung = data.index('Dudung')
print(f'Index dudung berada di = {index_dudung}')
# data.index('Usep') -> Eror karena di data ga ada usep

# Mengurutkan list (.sort())
print(f'Data angka sebeulum di sort = \n{data_angka}')
data_angka.sort()
print(f'Data angka setelah di sort = \n{data_angka}')

print(f'Data string sebelum di sort = \n{data}')
data.sort()
print(f'Data string setelah di sort = \n{data}')

# Balik listnya (.reverse())
data_angka.reverse()
data.reverse()
print(f'Data angka setelah di reverse = \n{data_angka}')
print(f'Data string setelah di reverse = \n{data}')