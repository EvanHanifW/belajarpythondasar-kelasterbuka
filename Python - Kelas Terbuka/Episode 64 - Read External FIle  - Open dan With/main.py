## tutorial membaca file eksternal

print(3*'=', 'Membaca file txt', 3*'=')
file = open("data.txt", mode="r")

print(f'status read : {file.readable()}')
print(f'status write : {file.writable()}')

## baca seluruh file
# print(file.read())

## baca perbaris
# print(file.readline(), end=' ')
# print(file.readline(), end=' ')

## baca semua baaris sebagai list
print(file.readlines())

print(f'apakah file sudah diclose : {file.closed}')
file.close()
print(f'apakah file sudah diclose : {file.closed}')

file = open("data.txt", mode="r")

print('\n', 3*'=', 'Membaca file txt dengan with', 3*'=')

with open('data.txt',mode='r') as file:
    content = file.readline()
    print(content,end='')
    print(f'apakah file sudah diclose : {file.closed}')
print(f'apakah file sudah diclose : {file.closed}')
