data = 'Ini adalah string'
print(data)
print(type(data))

# 1. Cara mambuat string

'''
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")


# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at') 
print('g\'day, isn\'t it?') 

# backlash
print("C:\\user\\Ucup")

# tab
print('Ucup\t\t\t\t\totong, jauhan')

# backspace 
print('Ucup \botong')

# newline
print('baris pertama\nbaris kedua') # LF -> line feed -> unix, macos, linux
print('baris pertama\rbaris kedua') # CR -> carriage return -> commodore, acorn, lisp
print('baris pertama\r\nbaris kedua') # CRLF -> line feed carriage return -> windows


# 3. String literal atau raw

# hati-hati
print('C:\new folder')

# menggunakan raw string
print(r'C:\new folder') 

# multiline literal string
print(
    '''
    Nama : Ucup
    Kelas : 3 SD
    '''
)

# multiline literal string dan RAW
print(
    r'''
    Nama : Ucup
    Kelas : 3 SD\new Normal
    Website : www.ucup.com/newID
    '''
)