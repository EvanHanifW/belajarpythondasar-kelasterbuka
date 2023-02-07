## Operasi

data = ['Ucup', 'Otong', 'Dudung']

# Mengambil data dari list (indexing [])

# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f'Panjang data : {panjang_data}')


## Manipulasi data list

# Menambahkan item pada list sesuai posisi (insert)
print(f'Data sebelum ditmambah = \n{data}')
data.insert(1, 'Asep')
print(f'Data sesudah ditambah = \n{data}')

# Menambah di akhir list (append)
data.append('jajang')
print(f'Data sesudah diappend = \n{data}')

# Menambahkan list dengan list (extend)
data_baru = ['Ujang', 'Usep', 'Evan', 'Hasna']
data.extend(data_baru)
print(f'Data gabungan = \n{data}')

# Merubah data (pake indexnig [])

# Meremove data
data.remove('Ujang')
print(f'Data remove = \n{data}')
# data.remove('usep') # eror karena data tidak ada -> yang ada Usep

# meremove data paling belakang
data.pop()
print(f'Data akhir = \n{data}')
data_akhir = data.pop()
print(f'Data terakhir = {data_akhir}')