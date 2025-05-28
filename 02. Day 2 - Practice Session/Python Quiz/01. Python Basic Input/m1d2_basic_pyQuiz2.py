print("=== Kalkulator Profil Produk ===")

produk = input("Masukkan nama produk: ")
harga = input("Masukkan harga satuan produk: ")
jumlah = input("Masukkan jumlah produk yang dibeli: ")
diskon = input("Masukkan diskon (dalam persen): ")

# Format nama produk
nama_format = produk.upper()

# Hitung total sebelum diskon
total = int(harga) * int(jumlah)

# Hitung besar diskon
nilai_diskon = total * (float(diskon) / 100)

# Hitung total akhir
total_akhir = total - nilai_diskon

# Cetak hasil
print("Produk:", nama_format)
print("Total sebelum diskon: Rp", total)
print("Diskon: Rp", nilai_diskon)
print("Total yang harus dibayar: Rp", total_akhir)
