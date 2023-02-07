data0 = [1,2]
data1 = [3,4]

list_biasa = [1,2,3,4]
print(f'List biasa = {list_biasa}')

list_2d = [data0, data1, 6, 8]
print(f'List 2d = {list_2d}')


# Contoh penggunaan
user0 = ['Ucup', 25, 'Laki-laki']
user1 = ['Evan', 18, 'Laki-laki']
user2 = ['Hasna', 18, 'Perempuan']

list_user = [user0, user1, user2]
print(f'User = {list_user}')

for user in list_user:
    print(f'nama\t: {user[0]}')
    print(f'umur\t: {user[1]}')
    print(f'gender\t: {user[2]}\n')


# Permasalahan dengan reference

list_copy = list_user.copy()
print(f'List copy = {list_copy}')
user0[0] = 'Reze'
print(f'List copy = {list_copy}')
print(f'List User = {list_user}')