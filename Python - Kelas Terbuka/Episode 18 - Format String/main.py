# format sting


# contoh generic
# string
nama = 'marlene'
format_str = f'hello {nama}'
print(format_str)


# boolean
boolean = True
format_str = f'Boolean = {boolean}'
print(format_str)


# angka
angka = 20202.1
format_str = f"angka = {angka}"
print(format_str)


# bilangan bulat
angka = 15
format_str = f"blangan bulat = {angka:d}"
print(format_str)

# bilangan jutaan
angka = 20000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2032003.54321
format_str = f"desimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2032003.54321
format_str = f"desimal = {angka:015.2f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f'plus = {angka_plus:+.2f}'
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f'persen = {persentase:.2%}'
print(format_persen)

# melakukan operasi aritmatika dalam placeholder
harga = 10000
jumlah = 5
print(f'harga total = {harga*jumlah}')

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f'binary = {bin(angka)}'
format_octal = f'octal = {oct(angka)}'
format_hex = f'hex = {hex(angka)}'

print(format_binary)
print(format_hex)
print(format_octal)