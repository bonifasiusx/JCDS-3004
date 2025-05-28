# Perbaiki bug dalam program ini agar dapat berjalan dengan baik
# Tujuan: Pembelian tiket konser musik

print("=== Selamat datang di Sistem Pembelian Tiket ===")

# Ambil input
nama = input("Masukkan nama lengkap: ")
umur = int(input("Masukkan umur: "))
email = input("Masukkan email: ")
jml_tiket = input("Masukkan jumlah tiket: ")

print("\n=== Validasi Data ===")

# Validasi umur
if umur >= 17:
    print("Umur valid.")
    boleh_daftar = True
else:
    print("Umur kamu belum cukup untuk mendaftar.")
    boleh_daftar = False

# Validasi email
if "@" in email and "." in email:
    print("Email valid.")
else:
    print("Format email tidak sesuai.")

# Validasi nama
if len(nama) > 0:
    print("Nama tercatat.")
else:
    print("Nama tidak boleh kosong")
    boleh_daftar = False

print("\n=== Total Harga Tiket ===")
# Total harga
harga_tiket = 100_000
total_harga = int(jml_tiket) * harga_tiket
print(f"Rp. {harga_tiket} x {jml_tiket} = {total_harga}")

if int(jml_tiket) > 2:
    diskon = total_harga * 0.2
    print("\nSelamat kamu mendapatkan diskon 20% !")
    total_harga = total_harga + diskon


# Kesimpulan
if boleh_daftar == True:
    print("\n Pendaftaran berhasil! Sampai jumpa di acara.")
else:
    print("\n Pendaftaran gagal. Silakan periksa data kamu.")
