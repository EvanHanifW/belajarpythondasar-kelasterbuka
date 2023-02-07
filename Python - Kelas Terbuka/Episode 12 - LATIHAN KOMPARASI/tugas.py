#-----0+++++5-----8++++++11-----
inputuser = float(input('Masukan angka :'))

isLebihDari0 = inputuser > 0
isKurangDari5 = inputuser < 5
isBetween0and5 = isLebihDari0 and isKurangDari5
isLebihDari8 = inputuser > 8
isKurangDari11 = inputuser < 11
isBetween8and11 = isLebihDari8 and isKurangDari11
isCorrect = isBetween0and5 or isBetween8and11
#print(isCorrect)


#+++++0-----5+++++8-----11++++++
inputuser = float(input('Masukan angka :'))

isKurangDari0 = inputuser < 0
isLebihDari5 = inputuser > 5
isKurangDari8 = inputuser < 8
isBetween5and8 = isLebihDari5 and isKurangDari8
isLebihDari11 = inputuser > 11
isCorrect = isKurangDari0 or isBetween5and8 or isLebihDari11
print(isCorrect)
