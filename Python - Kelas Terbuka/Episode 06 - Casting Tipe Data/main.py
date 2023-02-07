# Casting
# Merubah satu tipe ke tipe yang lain


# Integer
print('=========INTEGER========')
data_int = 9
print('Data = ', data_int, ', bertipe: ', type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print('Data = ', data_float, ', bertipe: ', type(data_float))
print('Data = ', data_str, ', bertipe: ', type(data_str))
print('Data = ', data_bool, ', bertipe: ', type(data_bool))


# Float
print('=========FLOAT========')
data_float = 9.5
print('Data = ', data_float, ', bertipe: ', type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print('Data = ', data_int, ', bertipe: ', type(data_int))
print('Data = ', data_str, ', bertipe: ', type(data_str))
print('Data = ', data_bool, ', bertipe: ', type(data_bool))


# BOOLEAN
print('=========BOOLEAN========')
data_bool = True
print('Data = ', data_bool, ', bertipe: ', type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print('Data = ', data_int, ', bertipe: ', type(data_int))
print('Data = ', data_str, ', bertipe: ', type(data_str))
print('Data = ', data_float, ', bertipe: ', type(data_float))

# String
print('=========STRING========')
data_str = 'ucup'
print('Data = ', data_str, ', bertipe: ', type(data_str))

data_int = int(data_str) # str harus angka
data_bool = bool(data_bool) # false jika string kosong
data_float = float(data_str) # str harus angka
print('Data = ', data_int, ', bertipe: ', type(data_int))
print('Data = ', data_bool, ', bertipe: ', type(data_bool))
print('Data = ', data_float, ', bertipe: ', type(data_float))