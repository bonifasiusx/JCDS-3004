# Allow variable to contain more than 1 value

# =========== list = [] =========== #

listContoh = ['hello', 1, 1, 3, True]
print(listContoh) # Print seluruh isi list
# ['hello', 1, 1, 3, True]

# Akses hanya 1 item dari dalam list berdasarkan indexing
print(listContoh[2]) # ATAU negative indexing --> print(listContoh[-3])
# 1 (Angka 1 yang kedua)

# Akses beberapa item dengan cara slicing
print(listContoh[:-1]) # ATAU print(listContoh[0:4])
# ['hello', 1, 1, 3]

# NOTES ---> (SLICING = AWAL (Kiri) : AKHIR (Kanan))
# print(listContoh[1:4])
print(listContoh[-4:-1]) # Negative indexing
# [1, 1, 3]

# extend = ['Item', 'Tambahan']
# listContoh.extend(extend) Nambahin Item > 1 ke dalam list
listContoh.append(False) # Nambahin item ke index paling akhir
listContoh.insert(2, 'satu satu') # Nambahin item ke index secara spesifiik
# ['hello', 'satu satu', 1, 1, 3, True, 'False']

listContoh.pop # Menghapus last item
listContoh.remove(1) # Akan menghapus '1' yang pertama ditemukan
# listContoh.pop(1) Menghapus item berdasarkan indexnya
# ['hello', 'satu satu', 1, 3, True, False]

# Menghapus seluruh item dari list tanpa mengapus listnya
# listContoh.clear() ---> listContoh = []

# For loop setiap item dari sebuah list
for item in listContoh:
    print(item) 

# Mencari / mencocokan item di dalam list
print()
if 'satu satu' in listContoh:
    print('Ada')
else:
    print('Gaada')

# Mencari item jika tidak tahu indexnya berapa
cari_index = listContoh.index('satu satu')
print(cari_index) # 1
# 'satu satu' muncul 1x dari listContoh

# Perhatikan cara sorting data dari sebuah list:
extend = ['Item', 'Tambahan', 'Latihan', 'List']
extendCopy = extend.copy() # Mehotd .copy()
extendCopy.sort(reverse=True) # Method .sort() berdiri sendiri

print(extendCopy)


# =========== tuple = () =========== #
# Tuple tidak bisa dimodifikasi tapi bisa di Concate
# --> tuple1 + tuple2 = (tuple1, tuple2)

# Contoh penggunaan tuple
tupleContoh = ('Bonifasius Sinurat', 'Laki-laki', 'Jakarta', 1998, 'Indonesia')


# ======== dictionary = {} ======== #
# KEY di Dictionary ---> INDEX di LIST
print()
dictContoh = { # 'nama', 'usia', 'pekerjaan', 'menikah' = Key/Index
    'nama' : 'Bonar',
    'usia' : 26,
    'pekerjaan' : 'Staff',
    'menikah' : False
} # 'Bonar', 26, 'Staff', False = Value

print(dictContoh)
print()
# Access Data di Dictionary
# print() + namaDict[namaKey] --> Cara 1
# print() + namaDict.get(namaKey) --> Cara 2

# Tambahin Data ke Dictionary
dictContoh['gender'] = 'pria'
print(dictContoh)

# Delete data
dictContoh.pop('menikah') # Menghapus sepasang Key-Values dari key 'menikah'
dictContoh.popitem() # Menghapus data Key-Val yang paling terakhir/kanan

# For Loop di Dictionary
# xxxxxxxxxx PELAJARI xxxxxxxxxx #
print()
for key in dictContoh: # Hanya looping key nya saja
    print(key)
print()
for key,val in dictContoh.items(): # Looping setiap Key-Val
    print(key,':', val)
    
print()
# ======== set = {val} ======== #
# Dengan kata lain ---> Himpunan
# Penulisan syntax langsung hanya bisa pilih salah satu (Key atau Values)
# Tidak berurutan ---> Tidak punya index ---> Gabisa akses data

contohSet = {'The Avangers', 'Iron Man 3', 'Avangers: Age of Ultron', 'Iron Man 3'}
print(contohSet) # Data duplikat langsung hilang
print()

# Mengakses data dari Set menggunakan for loop
for item in contohSet:
    print(item)
print()

# Menambah & Menghapus data ke Set
contohSet.add('Iron Man') # Tambah singular data kedalam set
contohSet.update({'Iron Man', 'Hulk'}) # Tambah data lebih dari 1
contohSet.remove('Iron Man 3') # Kalo make .pop() data yang kehapus itu random

print(contohSet)
print()




'''
    Fungsi dari set:
    - Menghilangkan duplikat dari sebuah data dari list/tuple (atau val dari sebuah Dict)
        ---> casting ke set ---> set{list/tuple}
        ---> data duplikat langsung hilang
'''