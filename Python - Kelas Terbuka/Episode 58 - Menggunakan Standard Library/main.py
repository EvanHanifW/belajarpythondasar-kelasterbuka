import datetime

data_waktu = datetime.datetime.now()
print(f' datetime now: {data_waktu}')
print(f' tahun: {data_waktu.year}')
print(f' hari: {data_waktu.strftime("%A")}')

from collections import Counter

data = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c']
data_count = Counter(data)

print(f'Data count = {data_count}')
print(f'Jumlah a = {data_count["a"]}')
print(f'Jumlah b = {data_count["b"]}')

import io

file = io.open('text.txt', 'r')
