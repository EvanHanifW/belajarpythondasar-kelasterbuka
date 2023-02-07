# membuat module matematika dengan import

from matematika import tambah, kali, pangkat
# from matematika import *

hasil_tambah = tambah(1,23,123,124,12,1)
print(f'Hasil tambah : {hasil_tambah}')

hasil_kali = kali(1,23,123,124,12,1)
print(f'Hasil kali : {hasil_kali}')

pangkat_3 = pangkat(3)
print(f'Pangkat 3 : {pangkat_3(5)}')