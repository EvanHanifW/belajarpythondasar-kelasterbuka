''' Fungsi dengan argument (input)'''

def hello_world(nama):
    ''' Fungsi hello world menerima input dengan variable nama'''
    print(f'Selamat datang {nama}')

def say_hi(list_peserta):
    '''Fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f'yang terhormat : {peserta}')

anggota_boyband = ['Evan', 'hanif', 'widiatama']

say_hi(anggota_boyband)