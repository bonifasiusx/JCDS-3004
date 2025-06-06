# ====== Python Function ====== #

# General Function
def contohFunct(angka1, angka2): # Contoh syntax -> range(1, 10)
    # syntax....
    # syntax....
    # syntax....
    # return [1]
    return angka1 + angka2 # [2]
    # Tujuan Return itu ada 2:
        # [1] Break di Loop == Return di Function
        # [2] Return value to the caller

# Lambda Function
lambda angka1,angka2: angka1 + angka2 # Lambda funct

# Funtion without Input Nor Output
def salam():
    print('Hai!')
    print('Semoga harimu menyenangkan\n')
    
salam()

# Funtion with Input but withput Output
namaUser = input('Masukkan nama: ')
usiaUser = input('Masukkan usia: ')

# Set & Default Parameter
def salamBalik(usia, nama='Unknown'): # Default Parameter harus selalu di akhir!
    if nama == 'Unknown':
        print(f'Saya berusia {usia}\n')
    else:
        print(f'Hai {nama}, usia Anda adalah {usia}\n')

salamBalik(usiaUser, namaUser)

# Parameter VS Arguments
salamBalik(usia=27, nama='Bonar')
# (usia,nama --> parameter) (=... --> argument)

# LIBRARY ---> CAPSTONE PROJECT
# tabulate

from prettytable import PrettyTable

print()
print('=====')
# COPY-PASTE dari script Exercise 4 Pt.2 Loop Statements
welcome = '\nSelamat Datang di Pasar Buah'

# Bagian Column
myProduct = PrettyTable(['Nama', 'Stok', 'Harga'])
# Bagian Rows
myProduct.add_row(['apel', 40, 10000])
myProduct.add_row(['jeruk', 30, 15000])
myProduct.add_row(['anggur', 20, 20000])

print(myProduct)


a = 2 and 3
print(a)

lee, kim, tim = 'x', None, ()
print(not lee if lee or kim else tim)



# =====================
