# operasi komparasi 
# hasilnya selalu boolean


# >,<,>=,<=,==,!=,is,is not
a = 4
b = 2

# lebih besar dari (>) 
# kurang dari (<) 
# lebih besar sama dengan (>=) 
# kurang dari sama dengan (<=)
# sama dengan (==) 
# tidak sama dengan (!=) 


# is membandingkan memory / objek
# is sebagai komparasi object identity
x = 5 # ini adalah assigment membuat object 
y = 6
print('nilai x: ', x, ' id x: ', hex(id(x)))
print('nilai y: ', y, ' id y: ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)