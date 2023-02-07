# looping dictionary

teman_teman = {
    'qih' : 'faqih',
    'ndi' : 'andi',
    'sat' : 'satya',
    'ka' : 'mazka'
}

# looping first try
for teman in teman_teman: # yang keluar cuma key
    print(teman)

# operator untuk mengambil item / iterables
keys = teman_teman.keys() # ambil iterables key
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values() # ambil iterables value
print(values)

for value in teman_teman.values():
    print(value)

items = teman_teman.items() # ambil iterasi key-value (items)
print(items)

for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f'key : {key}, values : {value}')
