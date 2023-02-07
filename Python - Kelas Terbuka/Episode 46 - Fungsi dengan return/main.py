''' Fungsi dengan kembalian '''

def kuadrat(input_angka):
    ''' Fungsi kuadrat'''

    output_kuadrat = input_angka ** 2
    return output_kuadrat

y = kuadrat(3)
y = 10 + kuadrat(16)
print(kuadrat(20))


# fungsi dengan banyak return
def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah, kurang, kali, bagi

k, l, m, n = operasi_matematika(9, 5)

print(f'Hasil tambah = {k}')
print(f'Hasil kurang = {l}')
print(f'Hasil kali = {m}')
print(f'Hasil bagi = {n}')
