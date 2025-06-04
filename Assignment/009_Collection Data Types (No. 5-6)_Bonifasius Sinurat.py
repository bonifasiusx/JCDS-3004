from tabulate import tabulate

# COPY-PASTE dari script Exercise 4 Pt.2 Loop Statements
welcome = '\nSelamat Datang di Pasar Buah\n'

# Tabel Produk
myProduct = [
    ['apel', 40, 10000],
    ['jeruk', 30, 15000],
    ['anggur', 20, 20000]
]

print(welcome) # Welcome di luar while loop supaya muncul hanya 1x (Pertama kali program dijalankan)

# MENU
list_menu = [
    '[1] Menampilkan daftar buah',
    '[2] Menambah buah',
    '[3] Menghapus buah',
    '[4] Membeli buah',
    '[0] Exit Program'
]

while True:
    PRODUCT = [] # List final untuk menampung Index + Items
    
    # Column List PRODUCT
    headers = ['Index', 'Nama', 'Stok', 'Harga']
    
    # Menu di dalam Loop agar konsisten ditampilkan ke User
    print('\nList Menu:')
    for menu in list_menu:
        print(menu)
        
    user_menu_option = input('\nSilahkan pilih menu: ')
    # Loop user sampai kasih input yang valid
    
    # LOOP -> USER HANYA BISA KELUAR DARI LOOP JIKA MEMILIH EXIT MENU
    if user_menu_option == '0': # Buat Exit Program dulu supaya ada path untuk break paksa while loop
        # [0] Exit Program
        print('\nProgram Selesai')
        break
    
    # LOOP -> USER PILIH MENU [1] MENAMPILKAN BUAH
    if user_menu_option == '1': # [1] Menampilkan Daftar Buah
        # Enumerate untuk membuat index di List final
        for idx, item in enumerate(myProduct, start=1):
            PRODUCT.append([idx] + item)
            
        print('\nDaftar Buah:\n')
        print(tabulate(PRODUCT, headers, tablefmt="grid", rowalign='right'))
    
    elif user_menu_option == '2': # [2] Menambah Buah
        add_product = input('\nMasukkan Nama Buah\t: ').lower() # Biar hasilnya rapih pas pake .title()
        add_stock = input('Masukkan Stock Buah\t: ')
        add_price = input('Masukkan Harga Buah\t: ')
        
        # Looping sampai user kasih input yang valid
        if not add_price.isdigit() or not add_stock.isdigit():
            print('\nInput tidak dikenali, silahkan coba lagi.')
            continue
        else:
            # Membuat list baru
            new_product = [add_product, add_stock, add_price]
            myProduct.append(new_product) # Append ke list awal
            
            for idx, item in enumerate(myProduct, start=1):
                PRODUCT.append([idx] + item) # Append ke list final
                
            # Tampilkan Hasil Update Data Daftar Buah
            print('\nDaftar Buah:\n')
            print(tabulate(PRODUCT, headers, tablefmt="grid", rowalign='right'))
            # continue
        print() 
    elif user_menu_option == '3': # [3] Menghapus Buah
        del_product = input('\nMasukkan index buah yang ingin dihapus: ')
        
        # Loop user sampai kasih input yang valid
        if not del_product.isdigit():
            print('\nInvalid Input, silahkan coba lagi.')
            continue
        
        idx_del = int(del_product)    
        # Jika index yang di-input > jumlah data PRODUCT atau kurang dari 1
        if idx_del > len(myProduct) or idx_del < 1:
            print('\nIndex tidak dikenali, silahkan coba lagi.')
            # continue
        # Hapus anak list dari list final PRODUCT berdasarkan index (dikurangi 1 karena list 0-indexed)
        else:
            del myProduct[idx_del - 1]
            # Tampilkan Hasil Data Buah Setelah Delete
            for idx, item in enumerate(myProduct, start=1):
                PRODUCT.append([idx] + item)
                
            print('\nDaftar Buah:\n')
            print(tabulate(PRODUCT, headers, tablefmt="grid", rowalign='right'))
            # continue
        print()
    elif user_menu_option == '4': # [4] Membeli Buah
        # Column List Cart
        cart = []
        cart_header = ['Nama', 'Qty', 'Harga']
        
        while True:        
            idx_user = input('\nMasukkan index buah yang ingin dibeli: ')
            qty = input('\nMasukkan jumlah: ')
            
            
            idx = int(idx_user) - 1
            qty = int(qty)
            
            if idx < 0 or idx >= len(myProduct):
                print('\nIndex tidak tersedia.')
                continue
            
            buah = myProduct[idx][0]
            stock = int(myProduct[idx][1])
            price = int(myProduct[idx][2])
            
            if qty > stock:
                print(f'Maaf stok tidak cukup. Stok {buah} tinggal {stock}.')
            else:
                total = price * qty
                print(f'Anda membeli {qty} {buah} seharga Rp {total}')
                cart.append([buah, qty, price, total])
                myProduct[idx][1] = stock - qty  # update stok

            print('\nShopping Cart:')
            print(tabulate(cart, cart_header, tablefmt="grid", rowalign='right'))
            
            buy_more = input('Mau beli yang lain (Ya/Tidak): ')
            if buy_more.lower() != 'ya':
                break
    else:
        print('\nPilihan tidak tersedia, silahkan coba lagi.')

# ===================================== #

    # FLOW [4]
    # elif user_menu_option == '4':
    # [4] MEMBELI BUAH
        # Loop:
        #     Input User ---> Beli product berdasarkan index
        #         Validasi Stok
        #         Isi Cart Sementara
        #         Validasi Cart
        #         Isi Cart Sementara
        #     Daftar Belanja
        # Kondisi Transaksi
    # else:
    #     print('\nInvalid. Silahkan pilih menu yang tersedia')
    
# ===================================== #

# print('\nDetail Belanja\n')

# total_apel = input_apel * harga_apel
# print(f'Apel : {input_apel} x {harga_apel} = {total_apel}')

# total_jeruk = input_jeruk * harga_jeruk
# print(f'Jeruk : {input_jeruk} x {harga_jeruk} = {total_jeruk}')

# total_anggur = input_anggur * harga_anggur
# print(f'Anggur : {input_anggur} x {harga_anggur} = {total_anggur}')

# total_harga = total_apel + total_jeruk + total_anggur
# print(f'\nTotal : Rp {total_harga}')

# # Looping Statements saat transaksi berlangsung
# transaksi = True

# while transaksi:    
#     # 10
#     # Minta uang dari user dan hitung uang dengan total harga belanja
#     uang = int(input('\nMasukkan jumlah uang: '))
    
#     while uang < total_harga:
#         # Skenario Transaksi GAGAL sampai kondisi uang > total_harga tercapai
#         print('\nTransaksi GAGAL')
#         print(f'Pembayaran diterima: Rp {uang}')
#         print(f'Kekurangan pembayaran sebesar: Rp {total_harga - uang}\n')
        
#         uang_tambahan = int(input('Masukkan Dana Tambahan: '))
#         uang += uang_tambahan # Selalu update jumlah uang di dalam loop
    
#         if uang > total_harga: # Keluar dari while loop uang < total_harga
#             break
#         else:
#             continue # Transaksi GAGAL sampai kondisi uang > total_harga tercapai
    
#     if uang > total_harga: # Jika uang > total_harga, kasih kembalian
#         kembalian = uang - total_harga
#         print('\nTransaksi Selesai!')
#         print(f'Uang kembali (Rp {kembalian})')
#         print('Terima kasih\n')
#         transaksi = False # Keluar dari while loop transaksi
        
#     elif uang == total_harga:
#         print('\nTransaksi Selesai!')
#         print('Terima kasih\n')
#         transaksi = False
