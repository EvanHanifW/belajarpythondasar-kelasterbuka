# Operasi Aritmatika

a = 10 
b = 3 


# Operasi tambah (+)
hasil = a + b 
print(a, '+', b, '=', hasil)

# Operasi pengurangan (-)
hasil = a - b 
print(a, '-', b, '=', hasil)

# Operasi perkalian (*)
hasil = a * b 
print(a, '*', b, '=', hasil)

# Operasi pembagian (/)
hasil = a / b 
print(a, '/', b, '=', hasil)

# Operasi eksponen/pangkat (**)
hasil = a ** b 
print(a, '**', b, '=', hasil)

# Operasi modulus (%)
hasil = a % b 
print(a, '%', b, '=', hasil)

# Operasi floor division (//)
hasil = a // b 
print(a, '//', b, '=', hasil)


# prioritas operasi
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-teman * / % //
    4. pertambahan dan pengurangan + -
'''
x, y, z = 3, 2, 4
hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling awal
hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=',hasil)