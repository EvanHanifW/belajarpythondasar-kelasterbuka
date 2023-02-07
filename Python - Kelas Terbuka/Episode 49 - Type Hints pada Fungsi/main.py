''' Type hints untuk fingsi '''

# Bentuk standar fungsi

'''
def fungsi(parameter):
    hasil = parameter ** 2
    print(hasil)

fungsi(1)
fungsi('Ucup')
fungsi(True)
'''

# penggunaan type hints

def sepuluh_pangkat(argument:int) -> int:
    ''' Fungsi dengan hints'''
    return 10 ** argument

hasil = sepuluh_pangkat(2.5)
print(hasil)

import string

def display(argument:string):
    print(argument)