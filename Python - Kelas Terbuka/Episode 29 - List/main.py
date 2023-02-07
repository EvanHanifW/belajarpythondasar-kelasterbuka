## ----- List -----

# Kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)

# Kumpulan data string
data_string = ['aku', 'dia', 'sama sama', 'kos kosan']
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan data campuran
data_campuran = [1, True, 'Otong', 'Ucup', 5, False, 2, 3]
print(data_campuran)


## Cara alternatif membuat list
data_range = range(0,10,2) # Range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# List comprehension
data_list_for = [i ** 3 for i in range(0,10)]
print(data_list_for)

# list comprehension with if
list_for_if = [i for i in range(0,10) if i % 2 == 0]
print(list_for_if)