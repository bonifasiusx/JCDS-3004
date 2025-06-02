# Buat program
# ================================================
# PROGRAM PEMANTAUAN KONSUMSI AIR HARIAN
# ================================================

# Deskripsi:
# Program ini digunakan oleh pengguna untuk mencatat dan mengevaluasi jumlah air
# yang dikonsumsi setiap hari dalam periode pemantauan tertentu.
# Program meminta input pengguna dan mengevaluasi konsumsi air harian berdasarkan target.

# Fitur program:
# 1. Meminta input:
#    - Nama pengguna
#    - Target konsumsi air per hari (liter)
#    - Jumlah hari pemantauan

# 2. Untuk setiap hari:
#    - Meminta input konsumsi air (liter)
#    - Jika konsumsi == 0:
#        - Cetak "Hari ini kamu lupa minum, lanjut besok."
#        - Gunakan `continue` untuk melanjutkan ke hari berikutnya
#    - Jika konsumsi > 5:
#        - Cetak "Terlalu banyak konsumsi! Program dihentikan."
#        - Gunakan `break` untuk menghentikan program
#    - Jika konsumsi valid (antara 0 dan 5 liter):
#        - Jika konsumsi >= target → Cetak "Target tercapai!"
#        - Jika konsumsi < target  → Cetak "Kurang minum."

# 3. Setelah loop selesai:
#    - Hitung total konsumsi air dari hari-hari yang valid
#    - Hitung rata-rata konsumsi harian dari hari-hari valid

# 4. Tampilkan laporan ringkas (summary report) berisi:
#    - Nama pengguna
#    - Jumlah hari terpantau valid
#    - Total konsumsi air
#    - Rata-rata konsumsi per hari

# Catatan penting:
# Tidak boleh menggunakan list, tuple, atau tipe data koleksi lainnya.
# Materi terbatas pada: variabel, input, tipe data dasar, perhitungan, loop, if, break, continue


"""Contoh output yang diharapkan

=== Pemantauan Konsumsi Air Harian ===

Masukkan nama: Rina
Target konsumsi per hari (liter): 2
Jumlah hari pemantauan: 3

Hari ke-1
Masukkan konsumsi air hari ini: 2.5
Target tercapai!

Hari ke-2
Masukkan konsumsi air hari ini: 0
Hari ini kamu lupa minum, lanjut besok.

Hari ke-3
Masukkan konsumsi air hari ini: 6
Terlalu banyak konsumsi! Program dihentikan.

=== Summary Report ===
Nama: Rina
Jumlah hari terpantau: 2
Total konsumsi air: 4.0 liter
Rata-rata konsumsi: 2.0 liter/hari
"""

# Buat kode anda disini
