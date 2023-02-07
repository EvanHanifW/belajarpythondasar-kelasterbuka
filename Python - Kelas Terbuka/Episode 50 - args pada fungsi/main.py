''' *args '''

# memasukan data/argument

def fungsi(nama, tinggi, berat):
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
fungsi('ucup', 170, 40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
fungsi(['ucup', 170, 40])

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')

fungsi('dudung', 120, 120)

# studi kasus
def tambah(*data):
    # data tipenya tuple dan bisa diiterasi
    output = 0
    for angka in data:
        output += angka
    return output

print(tambah(1,23,131,32))
print(tambah(5,1))