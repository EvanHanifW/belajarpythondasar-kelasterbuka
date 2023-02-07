# 1. mode write -> dia akan membuat file baru jika tidak ada, 
# lalu akan overwrite isinya

with open('data1.txt', mode='w', encoding='utf-8') as file:
    file.write('jon si jony')

with open('data1.txt', mode='w', encoding='utf-8') as file:
    file.write('evan')

with open('data1.txt', mode='w', encoding='utf-8') as file:
    file.write('overwrite')

# 2. mode append
with open('data2.txt', mode='w', encoding='utf-8') as file:
    file.write('jon si jony\n')

with open('data2.txt', mode='a', encoding='utf-8') as file:
    file.write('jon si jony 22\n')

with open('data2.txt', mode='a', encoding='utf-8') as file:
    file.write('tambah lagi append\n')

# 3. mode r+
with open('data3.txt', 'w', encoding='utf-8') as file:
    file.write('data 3 \n')

with open('data3.txt', 'r+', encoding='utf-8') as file:
    file.write('baris 1 \n')
    file.write('baris 2 \n')
    file.write('baris 3 \n')

with open('data3.txt', 'r+', encoding='utf-8') as file:
    data = file.read()
    print(data)

with open('data3.txt', 'r+', encoding='utf-8') as file:
    file.write('otong surotong pie to tong\n') # menimpa isi teks sesuai dengan panjang data

