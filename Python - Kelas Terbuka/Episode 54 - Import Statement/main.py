# import

# fungsi untuk mengambil program 
# dari file external .py

# 1. untuk menyambung program dari external
import program_print
import program_siucup


# 2. import dengan data
import variabel
import kucuy

# data ada di namespace variable
print(variabel.data)
print(kucuy.data)


# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(4, 5)
print(hasil)
