# Date and time (latihan)


import datetime as dt

print('Silahkan masukan tanggal, \nbulan, dan tahun lahir anda')
tanggal = int(input('Tanggal \t: '))
bulan = int(input('Bulan \t\t: '))
tahun = int(input('Tahun \t\t: '))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f'tanggal_lahir lahir anda adalah : {tanggal_lahir}')
print(f'Hari nya adalah : {tanggal_lahir:%A}')

hari_ini = dt.date.today()
print(f'hari ini tanggal : {hari_ini}')
umur = hari_ini - tanggal_lahir
umur_tahun = umur.days // 365
print(f'Umur anda adalah: {umur_tahun} tahun')