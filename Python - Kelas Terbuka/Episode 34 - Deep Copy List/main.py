data0 = [1,2]
data1 = [3,4]

data2d = [data0, data1, 10]


# Shallow copy
data2dcopy = data2d.copy() # -> Shallow copy

print(f'Data 2d = {data2d}')
print(f'Data 2d copy= {data2dcopy}')

# mengambil data dari nested list
data = data2d[0][1]
print(f'Data = {data}')

# address
print(f'Address data2d asli = {hex(id(data2d))}')
print(f'Address data2d copy = {hex(id(data2dcopy))}')

print('Address dari member ke-1')
print(f'Address data2d asli = {hex(id(data2d[0]))}')
print(f'Address data2d copy = {hex(id(data2dcopy[0]))}')

data2d[1][0] = 5
data2d[2] = 9
print(f'Data = {data2d}')
print(f'Data copy = {data2dcopy}')


# Deep copy
from copy import deepcopy

data2d = [data0, data1, 10]
data2ddeepcopy = deepcopy(data2d)

print(f'Address data2d asli = {hex(id(data2d))}')
print(f'Address data2d deep = {hex(id(data2ddeepcopy))}')

print(f'Address data2d asli = {hex(id(data2d[0]))}')
print(f'Address data2d deep = {hex(id(data2ddeepcopy[0]))}')

data2d[0][1] = 30
print(f'Data 2d = {data2d}')
print(f'Data 2d copy= {data2dcopy}')
print(f'Data 2d deep= {data2ddeepcopy}')