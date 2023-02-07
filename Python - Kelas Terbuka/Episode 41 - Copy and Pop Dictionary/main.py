# copy dictionary

teman_teman = {
    'qih' : 'faqih',
    'ndi' : 'andi',
    'sat' : 'satya',
    'ka' : 'mazka'
}

friends = teman_teman.copy()

print(f'teman-teman : {teman_teman} \n')
print(f'friends : {friends}\n\n')

teman_teman['qih'] = 'abdullah faqih'

print(f'teman-teman : {teman_teman} \n')
print(f'friends : {friends}\n\n')


# pop dictionary (berdasarkan key)
dataFaqih = friends.pop('qih') # mentranfser item (dari friends -> datafaqih)
print(f'data faqih = {dataFaqih}\n')
print(f'friends = {friends}\n')

# popitem dictionary (ambil key value yang terakhir aja)
dataTerakhir = friends.popitem()
print(f'data terakhir = {dataTerakhir}\n')
print(f'friends = {friends}\n')
