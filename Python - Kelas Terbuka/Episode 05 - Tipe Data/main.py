# Tipe data: Angka satuan tanpa koma (Integer)
data_integer = 11
print('data : ', data_integer)
print('- bertipe : ', type(data_integer))


# Tipe data: angka dengan koma (Float)
data_float = 11.5
print('data : ', data_float)
print('- bertipe : ', type(data_float))


# Tipe data: kumpulan karakter (String)
data_string = '11'
print('data : ', data_string)
print('- bertipe : ', type(data_string))


# Tipe data: biner true/false (Boolean)
data_bool = False
print('data : ', data_bool)
print('- bertipe : ', type(data_bool))



## Tipe data khusus
# Bilangan kompleks
data_complex = complex(5,6)
print('data : ', data_complex)
print('- bertipe : ', type(data_complex))



# Tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(5.6)
print('data : ', data_c_double)
print('- bertipe : ', type(data_c_double))