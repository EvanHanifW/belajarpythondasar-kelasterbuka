# Latihan logika dan komparasi
# membuat gabungan area rentang dari angka


# ++++++3------10++++++
inputuser = float(input('Masukan angka yang bernilai\nkurang dari 3\natau lebih dari 10:\n'))

isKurangDari = (inputuser < 3)
isLebihDari = (inputuser > 10)
isCorrect = isKurangDari or isLebihDari
print('Angka yang anda masukan', isCorrect)


# ------3++++++10------
inputuser = float(input('Masukan angka yang bernilai\nlebih dari 3\natau kurang dari 10:\n'))

isLebihDari = (inputuser > 3)
isKurangDari = (inputuser < 10)
isCorrect = isKurangDari and isLebihDari
print('Angka yang anda masukan', isCorrect)