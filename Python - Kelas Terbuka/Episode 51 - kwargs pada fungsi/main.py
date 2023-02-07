''' **kwargs '''

def fungsi(nama, tinggi, berat):
    ''' Fungsi biasa '''
    print(f'{nama}, {tinggi}, {berat}')

fungsi('ucup', 40, 80)

def fungsi_kwargs(**kwargs):
    ''' Fungsi kwargs '''

    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']

    print(f'{nama}, {tinggi}, {berat}')

fungsi_kwargs(nama='ucup', tinggi=50, berat=50)
    

# studi kasus

def math(*numbers, **kwargs):
    option = kwargs['option']
    hasil = 0

    if option == 'tambah':

        for angka in numbers:
            hasil += angka
    
    if option == 'kurang':

        for angka in numbers:
            hasil -= angka

    return hasil
print(math(1,23,14,12,31,1, option='tambah'))