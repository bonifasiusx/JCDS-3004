# # 1
# print('No. 1')
# print('=====')

# for n in range(1,10):
#     if n == 1 or n == 3 or n % 2 == 0:
#         pass
#     else:
#         print(n)
#         break

# # 3
# print()
# print('No. 3')
# print('=====')

# symbol = 'X'
# space = ''
# length = 9

# for i in range(1,10):
#     print(f'{space * (length / 2)}{symbol}')


# # 4
# print()
# print('No. 4')
# print('=====')

# # Palindrom cek: KataK, TacoCat, lEveL, NoOn, kaSur inI ruSak
# cek_palindrom = input('Masukkan kata: ')

# for huruf in cek_palindrom:
#     if cek_palindrom.lower() == cek_palindrom[::-1].lower():
#         print(f'\'{cek_palindrom.lower()}\' adalah sebuah palindrom!')
#         break

# # 5
# print()
# print('No. 5')
# print('=====')

# cek_pangram = input('Masukkan kalimat: ')
# letters = 'abcdefghijklmnopqrstuvwxyz'
# # SAMPE SINI SOB #
# for pangram in range(len(letters) - len(cek_pangram) + 1):
#     if cek_pangram[pangram : pangram + len(cek_pangram)] == letters:
#         print('Kalimat tersebut adalah pangram!')


# COPY-PASTE Jawaban No. 4 dan 10 dari script Exercise Day 2 Python Fundamental
# No. 6
stok_apel = 20
stok_jeruk = 30
stok_anggur = 40

# 4
harga_apel = 10000
harga_jeruk = 15000
harga_anggur = 20000

# Looping Statements Exercise 4 Pt.2
stok = True

while stok:
    # Cast str ke int supaya bisa dicari total harganya
    input_apel = int(input('Masukkan Jumlah Apel : '))
    input_jeruk = int(input('Masukkan Jumlah Jeruk : '))
    input_anggur = int(input('Masukkan Jumlah Anggur : '))

    if input_apel > stok_apel:
        print(f'\nMaaf, stok apel yang tersedia hanya {stok_apel}, silahkan coba lagi.\n') 
    elif input_jeruk > stok_jeruk:
        print(f'\nMaaf, stok jeruk yang tersedia hanya {stok_jeruk}, silahkan coba lagi.\n')
    elif input_anggur > stok_anggur:
        print(f'\nMaaf, stok anggur yang tersedia hanya {stok_anggur}, silahkan coba lagi.\n')
    # Jika seluruh input apel, jeruk dan anggur <= stok masing-masing barang;
    elif input_apel <= stok_apel and input_jeruk <= stok_jeruk and input_anggur <= stok_anggur:
        # ---> Lanjut ke Detail Belanja    
        stok = False

print('\nDetail Belanja\n')

total_apel = input_apel * harga_apel
print(f'Apel : {input_apel} x {harga_apel} = {total_apel}')

total_jeruk = input_jeruk * harga_jeruk
print(f'Jeruk : {input_jeruk} x {harga_jeruk} = {total_jeruk}')

total_anggur = input_anggur * harga_anggur
print(f'Anggur : {input_anggur} x {harga_anggur} = {total_anggur}')

total_harga = total_apel + total_jeruk + total_anggur
print(f'\nTotal : Rp {total_harga}')

# Looping Statements saat transaksi berlangsung
transaksi = True

while transaksi:    
    # 10
    # Minta uang dari user dan hitung uang dengan total harga belanja
    uang = int(input('\nMasukkan jumlah uang: '))
    
    while uang < total_harga:
        # Skenario Transaksi GAGAL sampai kondisi uang > total_harga tercapai
        print('\nTransaksi GAGAL')
        print(f'Pembayaran diterima: Rp {uang}')
        print(f'Kekurangan pembayaran sebesar: Rp {total_harga - uang}\n')
        
        uang_tambahan = int(input('Masukkan Dana Tambahan: '))
        uang += uang_tambahan # Selalu update jumlah uang di dalam loop
    
        if uang > total_harga: # Keluar dari while loop uang < total_harga
            break
        else:
            continue # Transaksi GAGAL sampai kondisi uang > total_harga tercapai
    
    if uang > total_harga: # Jika uang > total_harga, kasih kembalian
        kembalian = uang - total_harga
        print('\nTransaksi Selesai!')
        print(f'Uang kembali (Rp {kembalian})')
        print('Terima kasih\n')
        transaksi = False # Keluar dari while loop transaksi
        
    elif uang == total_harga:
        print('\nTransaksi Selesai!')
        print('Terima kasih\n')
        transaksi = False
                   
