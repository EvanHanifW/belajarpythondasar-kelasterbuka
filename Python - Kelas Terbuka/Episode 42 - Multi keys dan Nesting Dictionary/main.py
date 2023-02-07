import datetime

mahasiswa1 = {
    'nama':'Evan Widiatama',
    'nim':'192399219',
    'sks_lulus':130,
    'beasiswa':True,
    'lahir':datetime.datetime(2004,10,4)
}

mahasiswa2 = {
    'nama':'Khairunnisa',
    'nim':'19239921239',
    'sks_lulus':140,
    'beasiswa':True,
    'lahir':datetime.datetime(2004,10,14)
}

mahasiswa3 = {
    'nama':'Evan Hanif',
    'nim':'19239921914',
    'sks_lulus':150,
    'beasiswa':True,
    'lahir':datetime.datetime(2004,11,4)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3,
}
print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print('-'*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
