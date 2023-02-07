# Ambil input dari user

# Data yang diinput pasti string
data = input('Masukan data: ')
print('Data dari user: ', data, ', bertipe: ', type(data))


# Jika menginginkan tipe data lain, perluu dilakukan casting
data_int = int(input('Masukan angka: '))
print('Data dari user: ', data_int, ', bertipe: ', type(data_int))


# Boolean? -> Perlu di casting ke int dulu
data_bool = bool(int(input('Masukan nilai boolean: ')))
print('Data dari user: ', data_bool, ', bertipe : ', type(data_bool))