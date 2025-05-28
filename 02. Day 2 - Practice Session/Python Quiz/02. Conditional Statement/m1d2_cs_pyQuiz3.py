# Lengkapi kode berikut agar program dapat berjalan dengan baik

# Studi Kasus
# Sistem Penyaringan Data Calon Responden Survey

# Deskripsi
# Sebagai seorang data analyst, kamu akan menyaring data responden sebelum mereka bisa diikutkan ke dalam sebuah survei online. 
# Kriteria kelayakan mereka tergantung pada:
# - Usia
# - Kota domisili
# - Frekuensi penggunaan internet
# - Apakah bersedia mengisi survei
# Setelah responden lolos kriteria, sistem akan mengestimasi reward yang akan diberikan berdasarkan profilnya.

print("=== Sistem Penyaringan Responden Survei ===")

# Ambil input dari pengguna
nama = input("Masukkan nama lengkap: ")
usia = int(input("Masukkan usia Anda: "))
kota = input("Kota domisili: ").lower()
internet_harian = int(input("Berapa jam per hari Anda menggunakan internet?: "))
bersedia = input("Apakah Anda bersedia mengisi survei? (ya/tidak): ").lower()

# Inisialisasi status
layak = False
reward = 0

# TODO: Tambahkan pengecekan kelayakan
# Syarat:
# - Usia antara 18–45 tahun
# - Domisili di kota target: jakarta, bandung, surabaya
# - Penggunaan internet minimal 2 jam/hari
# - Menjawab "ya" untuk kesediaan

if usia >= 18 and usia <= 45:
    layak = True
    print(f"\n{nama} lolos sebagai responden.")

    # TODO: Estimasi reward
    # Jika internet_harian >= 5 -> reward = 50000
    # Jika 3 ≤ internet_harian < 5 -> reward = 35000
    # Jika < 3 -> reward = 20000

    if internet_harian >= 5:
        reward = 50000
    elif internet_harian >= 3 and internet_harian < 5:
        reward = 35000
    else:
        reward = 20000

    # TODO: Cetak ringkasan hasil
if layak == True:
    print(f"Estimasi reward untuk {nama} adalah Rp{reward:,}")
else:
    print(f"\nMaaf {nama}, Anda tidak memenuhi kriteria responden.")

print("\n=== Proses Seleksi Selesai ===")
