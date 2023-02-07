print('\nPROGRAM KONVERSI TEMPERATUR FAHRENHEIT KE KELVIN\n')


# kelvin ke fahrenheit 
kelvin = int(input('Masukan suhu dalam kelvin : '))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print('Suhu di kelvin ', kelvin, ' suhu di fahrenheit ', fahrenheit)

# fahrenheit ke kelvin
fahrenheit = int(input('Masukan suhu dalam fahrenheit : '))
celcius = (5/9)*(fahrenheit - 32)
kelvin = celcius + 273
print('Suhu di fahrenheit ', celcius, ' suhu di kelvin ', kelvin)