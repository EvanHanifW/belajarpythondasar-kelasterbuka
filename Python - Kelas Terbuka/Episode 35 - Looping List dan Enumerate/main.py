# looping dari list


# for loop
print('For loop')
kumpulan_angka = [1,2,3,44124,124,1,32,2]

for angka in kumpulan_angka:
    print(f'angka = {angka}')

# for loop dan range
print('\n for loop dan range')
kumpulan_angka = [1,2,3,44124,124,1,32,2]
PANJANG_ANGKA = len(kumpulan_angka)

for i in range(PANJANG_ANGKA):
    print(f'angka = {kumpulan_angka[i]}')

# while loop
print('\n while loop')
kumpulan_angka = [1,2,3,44124,124,1,32,2]
angka_kuadrat = [i**2 for i in kumpulan_angka]
PANJANG_ANGKA = len(kumpulan_angka)
i = 0

while i < PANJANG_ANGKA:
    print(f'angka = {kumpulan_angka[i]}')
    i += 1


## list comprehension
print('\n list comprehension')
data = ['evan', 18, 'ucup', 'otong', 'sotong', 43]

[print(f'data = {i}') for i in data]


# enumerate
print('\n enumerate')
data_list = ['evan', 18, 'ucup', 'otong', 'sotong', 43]

for index, data in enumerate(data_list):
    print(f'index = {index}, data = {data}')

