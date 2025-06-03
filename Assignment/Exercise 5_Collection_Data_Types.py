# 1. Cari angka terbesar dan terkecil dari list yang sudah diberikan tanpa menggunakan fungsi max(), min(), maupun sort() yang merupakan fungsi built-in python!

# 1
print('No. 1')
print('=====')

list = [23, 57, 76, 6, 60, 28, 30,
44, 85, 44, 97, 32, 71, 85,
46, 95, 29, 37, 13, 79, 15, 9,
23, 10, 22, 78, 46, 2, 99, 3]

# Ambil 1 angka dari data untuk mencari yang terbesar & terkecilnya
cari_angka_terbesar = 23
cari_angka_terkecil = 23

# Jika i >, re-assign variabel cari_angka.... sampai ketemu angka yang paling besar/kecil dari seluruh data di variabel list
for i in list:
    if i > cari_angka_terbesar:
        cari_angka_terbesar = i
    elif i < cari_angka_terkecil:
        cari_angka_terkecil = i
print(f'Max number: {cari_angka_terbesar}')
print(f'Min number: {cari_angka_terkecil}')

# 2
print()
print('No. 2')
print('=====')

id = [
'K0QY6', 'fJU08', 'K0QY6', 'VeZrS', 'jxjQ6', 'sjqom', 'AefAN', 'jxjQ6',
'S90wn', 'FZw7F', 'IgYbm', 'dD1ZM', 'sjqom', 'dD1ZM', 'fJU08', 'AefAN',
'jxjQ6', 'K0QY6', 'prdDz', 'dD1ZM', 'AefAN', 'WfgpU', 'VeZrS', 'sjqom'
]

# Casting jadi set supaya menghilangkan duplikat data
unique_ID = set(id) 
count_unique_ID = len(unique_ID) # Hitung jumlah data tanpa duplikat

for unique in unique_ID:
    print(f'Unique ID: {unique}')
print(f'\nID awal: {len(id)}')
# Hasil tidak perlu dicast balik ke list karena unique_ID -> imutable
print(f'ID unik terdapat sebanyak: {count_unique_ID}')
    
# 3
print()
print('No. 3')
print('=====')
import math # Import math untuk menghitung akar dari setiap n

list = [
  344, 838, 502, 262, 590, 959, 151, 491, 71, 980, 156, 13, 280, 615, 278, 185,
  851, 599, 947, 598, 961, 534, 633, 751, 836, 446, 7, 956, 335, 765, 600, 428,
  595, 478, 667, 628, 375, 402, 663, 728, 704, 182, 377, 380, 49, 253, 566,
  662, 492, 930, 285, 5, 467, 496, 421, 317, 774, 86, 942, 149, 270, 765, 357,
  373, 336, 63, 976, 509, 863, 139, 504, 321, 635, 96, 977, 538, 552, 683, 83,
  752, 576, 350, 538, 79, 164, 414, 579, 948, 971, 121, 354, 562, 562, 63, 385,
  185, 731, 872, 342, 898
]

total_square_number = [] # List baru untuk jumlah total angka yang ditemukan

for num in list: 
    num_result = math.sqrt(num) # Hitung akar dari setiap angka di list
    if int(num_result) == math.sqrt(num): # Cari angka yang int saja
        total_square_number.append(num) # Masukkan angka kedalam list baru

print(f'Output\nTotal square number: {len(total_square_number)}')
print(total_square_number)         

# 4
print()
print('No. 4')
print('=====')

movies1 = ['Witch Of Stone', 'Mice And Soldiers', ' Learning From The Ashes', 'Assassins Of Sorrow', 'Wand Of Next Year', 'Binding To Dreams']

movies2 = ['Soldiers And Visitors', 'Intelligence In Orbit', 'Wand Of Next Year', 'Birth Of The Sands', 'Assassins Of Sorrow']

# EXAMPLE 2 ---> Cek Penggunaan Huruf Besar-Kecil di Data
# movies1 = ['Horrors And Figures', 'Foreigner In The Library', ' Learning From The Ashes', 'Assassins Of Sorrow', 'Wand Of Next Year', ' Oblivious To The Country']

# movies2 = ['Soldiers And Visitors', 'Intelligence In Orbit', 'wand of next year','horrors and figures', 'assassins of sorrow']

# Cari total film berdasarkan data keseluruhan
total_movies = len(movies1 + movies2) # Total = 11
print(f'Total data = {total_movies}')

# for loop dengan .lower() agar huruf besar-kecil di data tidak mempengaruhi hasil
movies1 = [movie.lower() for movie in movies1]
movies2 = [movie.lower() for movie in movies2]

# Cast list menjadi set
movies1, movies2 = set(movies1), set(movies2)

# Cari film yang sama dari kedua set
same_movies = movies1.intersection(movies2)
print(f'Total film yang sama = {len(same_movies)}')
print('\nJudul film yang sama:')
for item in same_movies:
    print(f'{item}')

# Hitung kesamaan dari kedua list
similarity_level = len(same_movies) / total_movies * 100

# Pake round untuk menghasilkan 2 angka desimal
print(f'\nSimilarity Level: {round(similarity_level, 2)}%')

# 5
print()
print('No. 5')
print('=====')