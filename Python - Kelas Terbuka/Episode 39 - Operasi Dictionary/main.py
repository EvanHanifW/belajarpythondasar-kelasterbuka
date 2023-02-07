# operator dictionary

data_dict = {
    'cup' : 'ucup surucup',
    'tong' : 'otong surotomg',
    'dung' : 'dudung surudung'
}

# panjang dictionary
LEN_DICT = len(data_dict)
print(f'Panjang dictionary : {LEN_DICT}')

# mengecek key exist
KEY = 'cupa'
CHECK_KEY = KEY in data_dict
print(f'Apakah {KEY} ada di data_dict : {CHECK_KEY}')

# mengakses value (read) dengan get
print(data_dict['cup'])
print(data_dict.get('cup'))
print(data_dict.get('kis', f'{KEY} tidak ditemukan'))

# mengupdate data
data_dict['cup'] = 'ucup ganteng'
print(data_dict)
data_dict['van'] = 'evan hanif'
print(data_dict)

data_dict.update({'cup' : 'ucup furucup'})
print(data_dict)
data_dict.update({'hasna' : 'kairunisa'}) # kalo ga ada add aja
print(data_dict)

# mendelete data dict
del data_dict['van']
print(data_dict)
