tinggi_ketupat = 4
spasi = tinggi_ketupat // 2
tengah = tinggi_ketupat // 2 + 1
currLine = 1
countChar = 1

while currLine < tinggi_ketupat:

    print(' '*spasi, 'X'*countChar)

    currLine += 1
    spasi -= 1
    countChar += 2

