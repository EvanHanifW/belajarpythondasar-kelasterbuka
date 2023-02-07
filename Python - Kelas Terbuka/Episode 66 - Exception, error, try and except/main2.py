# contoh membuar excception

from numbers import Number

def tambah(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise 'input  harus angka'
    return a+b

print(tambah(5, 7))

angka = 0

try:
    hasil = 10/angka
except Exception as eror_message:
    print(eror_message)

try:
    hasil = 10/angka
except ZeroDivisionError as eror_message:
    print(eror_message)