#  Latihan konversi satuan temperature

# program konversi celcius ke satuan lain 

print('\n PROGRAM KONVERSI TEMPERATUR\n')

celcius = float(input('Masukan suhu dalam satuan celcius : '))
print('suhu adalah', celcius, 'Celcius')

# reamur 
reamur = (4/5) * celcius
print('Suhu dalam reamur adalah ', reamur, ' Reamur')

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print('Suhu dalam fahrenheit adalah ', fahrenheit, ' Fahrenheit')

# kelvin
kelvin = celcius + 273
print('suhu dalam kelvin adalah ', kelvin, ' kelvin')