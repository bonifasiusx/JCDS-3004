# # 1
# print('No. 1')
# print('=====')

# list = [23, 57, 76, 6, 60, 28, 30,
# 44, 85, 44, 97, 32, 71, 85,
# 46, 95, 29, 37, 13, 79, 15, 9,
# 23, 10, 22, 78, 46, 2, 99, 3]

# # Ambil 1 angka dari data untuk mencari yang terbesar & terkecilnya
# cari_angka_terbesar = 23
# cari_angka_terkecil = 23

# # Jika i >, re-assign variabel cari_angka.... sampai ketemu angka yang paling besar/kecil dari seluruh data di variabel list
# for i in list:
#     if i > cari_angka_terbesar:
#         cari_angka_terbesar = i
#     elif i < cari_angka_terkecil:
#         cari_angka_terkecil = i
# print(f'Max number: {cari_angka_terbesar}')
# print(f'Min number: {cari_angka_terkecil}')

# # 2
# print()
# print('No. 2')
# print('=====')

# id = [
# 'K0QY6', 'fJU08', 'K0QY6', 'VeZrS', 'jxjQ6', 'sjqom', 'AefAN', 'jxjQ6',
# 'S90wn', 'FZw7F', 'IgYbm', 'dD1ZM', 'sjqom', 'dD1ZM', 'fJU08', 'AefAN',
# 'jxjQ6', 'K0QY6', 'prdDz', 'dD1ZM', 'AefAN', 'WfgpU', 'VeZrS', 'sjqom'
# ]

# # Casting jadi set supaya menghilangkan duplikat data
# unique_ID = set(id) 
# count_unique_ID = len(unique_ID) # Hitung jumlah data tanpa duplikat

# for unique in unique_ID:
#     print(f'Unique ID: {unique}')
# print(f'\nID awal: {len(id)}')
# # Hasil tidak perlu dicast balik ke list karena unique_ID -> imutable
# print(f'ID unik terdapat sebanyak: {count_unique_ID}')
    
# # 3
# print()
# print('No. 3')
# print('=====')
# import math # Import math untuk menghitung akar dari setiap n

# list = [
#   344, 838, 502, 262, 590, 959, 151, 491, 71, 980, 156, 13, 280, 615, 278, 185,
#   851, 599, 947, 598, 961, 534, 633, 751, 836, 446, 7, 956, 335, 765, 600, 428,
#   595, 478, 667, 628, 375, 402, 663, 728, 704, 182, 377, 380, 49, 253, 566,
#   662, 492, 930, 285, 5, 467, 496, 421, 317, 774, 86, 942, 149, 270, 765, 357,
#   373, 336, 63, 976, 509, 863, 139, 504, 321, 635, 96, 977, 538, 552, 683, 83,
#   752, 576, 350, 538, 79, 164, 414, 579, 948, 971, 121, 354, 562, 562, 63, 385,
#   185, 731, 872, 342, 898
# ]

# total_square_number = [] # List baru untuk jumlah total angka yang ditemukan

# for num in list: 
#     num_result = math.sqrt(num) # Hitung akar dari setiap angka di list
#     if int(num_result) == math.sqrt(num): # Cari angka yang int saja
#         total_square_number.append(num) # Masukkan angka kedalam list baru

# print(f'Output\nTotal square number: {len(total_square_number)}')
# print(total_square_number)         

# # 4
# print()
# print('No. 4')
# print('=====')

# movies1 = ['Witch Of Stone', 'Mice And Soldiers', ' Learning From The Ashes', 'Assassins Of Sorrow', 'Wand Of Next Year', 'Binding To Dreams']

# movies2 = ['Soldiers And Visitors', 'Intelligence In Orbit', 'Wand Of Next Year', 'Birth Of The Sands', 'Assassins Of Sorrow']

# # EXAMPLE 2 ---> Cek Penggunaan Huruf Besar-Kecil di Data
# # movies1 = ['Horrors And Figures', 'Foreigner In The Library', ' Learning From The Ashes', 'Assassins Of Sorrow', 'Wand Of Next Year', ' Oblivious To The Country']

# # movies2 = ['Soldiers And Visitors', 'Intelligence In Orbit', 'wand of next year','horrors and figures', 'assassins of sorrow']

# # for loop dengan .lower() agar huruf besar-kecil di data tidak mempengaruhi hasil
# movies1 = [movie.lower() for movie in movies1]
# movies2 = [movie.lower() for movie in movies2]

# # Cari total film berdasarkan data keseluruhan
# movies1, movies2 = set(movies1), set(movies2)
# total_movies = movies1.union(movies2) # Menghilangkan data duplikat
# print(f'Total film = {len(total_movies)}')

# # Cari film yang sama dari kedua set
# same_movies = movies1.intersection(movies2)
# print(f'Total film yang sama = {len(same_movies)}')
# print('\nJudul film yang sama:')
# for item in same_movies:
#     print(f'{item}')

# # Hitung kesamaan dari kedua list
# similarity_level = len(same_movies) / len(total_movies) * 100

# # Pake round untuk menghasilkan 2 angka desimal
# print(f'\nSimilarity Level: {round(similarity_level, 2)}%')

# 5
print()
print('No. 5')
print('=====')
# COPY-PASTE dari script Exercise 4 Pt.2 Loop Statements
welcome = '\nSelamat Datang di Pasar Buah'

# Data Buah
# Pakai nested List untuk data buah-buahan
PRODUCT = [ # Update jumlah stok agar lebih relate dengan skenario asli
    ['apel', 40, 10000],
    ['jeruk', 30, 15000],
    ['anggur', 20, 20000]
]

print(welcome) # Welcome di luar while loop supaya muncul hanya 1x (Pertama kali program dijalankan)

# User Input Menu
# WHILE TRUE AGAR USER HANYA BISA KELUAR DARI LOOP JIKA MEMILIH EXIT MENU
while True:
    # Menu
    list_menu = [
        '[1] Menampilkan daftar buah',
        '[2] Menambah buah',
        '[3] Menghapus buah',
        '[4] Membeli buah',
        '[0] Exit Program'
    ]
    
    print('\nList Menu:')
    for menu in list_menu:
        print(menu)

    user_menu_option = input('\nSilahkan pilih menu: ')
    # Loop user sampai kasih input yang valid
    if not user_menu_option.isdigit():
        print('\nPilihan tidak tersedia, silahkan coba lagi.')
    elif user_menu_option == '0': # Buat Exit Program dulu supaya ada path untuk break paksa while loop
        # [0] Exit Program
        print('\nProgram Selesai')
        break
    elif user_menu_option == '1':
        # [1] Menampilkan Daftar Buah
        print('\nDaftar Buah:\n')
        # Menggunakan \t agar tampilan daftar buah dapat sejajar menurun kebawah
        print('Index\t| Nama\t\t\t| Stok     \t| Harga\t') 

        idx = 0 # Index dari 0 agar bisa bertambah seiring berjalannya for loop
        for product, stock, price in PRODUCT:
            idx += 1
            # {product} pakai .title() supaya huruf depan setiap nama buah jadi kapital
            print(f'{idx}\t| {product.title()}          \t| {stock} \t\t| {price}')
        continue # Keluar dari while loop Menu --> [1] Menampilkan Daftar Buah
    elif user_menu_option == '2':
        # [2] Menambah Buah
        while True: # Looping sampai user kasih input yang valid
            add_product = input('\nMasukkan Nama Buah\t: ').lower() # Biar hasilnya rapih pas pake .title()
            add_stock = input('Masukkan Stock Buah\t: ')
            add_price = input('Masukkan Harga Buah\t: ')
            # Looping sampai user kasih input yang valid
            if not add_price.isdigit() and not add_stock.isdigit():
                print('Input tidak dikenali, silahkan coba lagi.')
            else:
                new_product = [add_product, add_stock, add_price]
                PRODUCT.append(new_product)
                break # Keluar dari while loop User Input --> Tambah Buah
        print()

        # Tampilkan Hasil Update Data Daftar Buah 
        print('\nDaftar Buah:\n')
        print('Index\t| Nama\t\t\t| Stok     \t| Harga\t') 
        idx = 0
        for product, stock, price in PRODUCT:
            idx += 1
            print(f'{idx}\t| {product.title()}          \t| {stock} \t\t| {price}')
        continue # Keluar dari while loop Menu --> [2] Menambah Buah
    elif user_menu_option == '3':
        # [3] Menghapus Buah
        while True: # Looping sampai user kasih input yang valid
            del_product = input('\nMasukkan index buah yang ingin dihapus: ')
            # Loop user sampai kasih input yang valid
            if not del_product.isdigit():
                print('Index tidak dikenali, silahkan coba lagi.')
            elif int(del_product) > len(PRODUCT):
                # Jika index yang di-input > jumlah data PRODUCT
                print('Index tidak dikenali, silahkan coba lagi.')
            else:
                idx_del = int(del_product)
                # Hapus anak list dari list PRODUCT berdasarkan index
                del PRODUCT[idx_del-1]
                
                # Tampilkan Hasil Update Data Daftar Buah 
                print('\nDaftar Buah:\n')
                print('Index\t| Nama\t\t\t| Stok     \t| Harga\t') 
                idx = 0
                for product, stock, price in PRODUCT:
                    idx += 1
                    print(f'{idx}\t| {product.title()}          \t| {stock} \t\t| {price}')
            break # Keluar dari loop User Input --> Menghapus Buah
        print()
    elif user_menu_option == '4':
        # [4] MEMBELI BUAH
        # Loop:
            # Input User ---> Beli product berdasarkan index
                # Validasi Stok
                    # Isi Cart Sementara
                # Validasi Cart
                    # Isi Cart Sementara
            # Daftar Belanja
            # Kondisi Transaksi
        pass
    else:
        print('\nInvalid. Silahkan pilih menu yang tersedia')
    
print()
    

# # No. 6
# stok_apel = 20
# stok_jeruk = 30
# stok_anggur = 40

# # 4
# harga_apel = 10000
# harga_jeruk = 15000
# harga_anggur = 20000

# stok = True

# while stok:
#     # Cast str ke int supaya bisa dicari total harganya
#     input_apel = int(input('Masukkan Jumlah Apel : '))
#     input_jeruk = int(input('Masukkan Jumlah Jeruk : '))
#     input_anggur = int(input('Masukkan Jumlah Anggur : '))

#     if input_apel > stok_apel:
#         print(f'\nMaaf, stok apel yang tersedia hanya {stok_apel}, silahkan coba lagi.\n') 
#     elif input_jeruk > stok_jeruk:
#         print(f'\nMaaf, stok jeruk yang tersedia hanya {stok_jeruk}, silahkan coba lagi.\n')
#     elif input_anggur > stok_anggur:
#         print(f'\nMaaf, stok anggur yang tersedia hanya {stok_anggur}, silahkan coba lagi.\n')
#     # Jika seluruh input apel, jeruk dan anggur <= stok masing-masing barang;
#     elif input_apel <= stok_apel and input_jeruk <= stok_jeruk and input_anggur <= stok_anggur:
#         # ---> Lanjut ke Detail Belanja    
#         stok = False

# print('\nDetail Belanja\n')

# total_apel = input_apel * harga_apel
# print(f'Apel : {input_apel} x {harga_apel} = {total_apel}')

# total_jeruk = input_jeruk * harga_jeruk
# print(f'Jeruk : {input_jeruk} x {harga_jeruk} = {total_jeruk}')

# total_anggur = input_anggur * harga_anggur
# print(f'Anggur : {input_anggur} x {harga_anggur} = {total_anggur}')

# total_harga = total_apel + total_jeruk + total_anggur
# print(f'\nTotal : {total_harga}')

# # Looping Statements saat transaksi berlangsung
# transaksi = True

# while transaksi:    
#     # 10
#     # Minta uang dari user dan hitung uang dengan total harga belanja
#     uang = int(input('\nMasukkan jumlah uang : '))
#     kembalian = uang - total_harga
    
#     if uang > total_harga: # Jika uang > total_harga, kasih kembalian
#         print('\nTerima kasih')
#         print(f'Uang kembalian Anda : {kembalian}')
#         print('\nSampai jumpa lagi!')
#         transaksi = False
        
#     elif uang == total_harga:
#         print('\nTerima kasih')
#         print('\nSampai jumpa lagi!')
#         transaksi = False
        
#     else: # Jika uang < total_harga, tunjukin kurangnya
#         kekurangan = total_harga - uang
#         print('\nGagal melakukan pembayaran')
#         print(f'Pembayaran diterima: Rp {uang}\n')
#         print(f'Kekurangan pembayaran sebesar: Rp {kekurangan}\n')
        
#         # Looping lagi jika dana tambahan masih kurang, sampai lunas
#         pembayaran_tertunda = True
        
#         while pembayaran_tertunda:
#             uang_tambahan = int(input('Dana Tambahan: '))
            
#             if uang_tambahan < total_harga: # MASIH KE-RESET MULU COYY
#                 print(f'Pembayaran diterima: Rp {uang_tambahan}\n')
#                 uang_terkini = uang + uang_tambahan
#                 print(f'Kekurangan pembayaran sebesar: Rp {total_harga - uang_terkini}\n')
                
#             elif uang > total_harga:
#                 print('Pembayaran berhasil')
#                 print('\nTerima kasih')
#                 print(f'Uang kembalian Anda : {uang - total_harga}')
#                 pembayaran_tertunda = False
                
#             else:
#                 print('Pembayaran berhasil')
#                 print('\nTerima kasih')
#                 print('\nSampai jumpa lagi!')
#                 pembayaran_tertunda = False
#         transaksi = False
            
