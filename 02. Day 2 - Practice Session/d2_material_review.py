# === REVIEW MATERI PYTHON DASAR ===
# Dokumentasi ini menyajikan rangkuman fitur dasar Python secara praktikal
# dengan contoh langsung yang dapat dieksekusi sebagai latihan mandiri.

# 1. Variabel dan Tipe Data
# Variabel adalah tempat menyimpan nilai. Python otomatis mengenali tipe data.
# Tipe data dasar: str (string), int (integer), float (desimal)
nama = "Andi"           # Tipe data: str (string/teks)
umur = 25               # Tipe data: int (bilangan bulat)
berat = 70.5            # Tipe data: float (bilangan desimal)
print("1. Variabel dan Tipe Data:")
print("Nama:", nama)
print("Tipe:", type(nama))
print("Umur:", umur)
print("Tipe:", type(umur))
print("Berat:", berat)
print("Tipe:", type(berat))
print()

# 2. String Method
# Metode string digunakan untuk manipulasi teks, seperti mengubah huruf,
# mengganti bagian teks, dan menghitung panjang string.
greeting = "selamat pagi"
print("2. String Methods:")
print("Original:", greeting)
print("Upper:", greeting.upper())      # Ubah ke huruf besar semua
print("Lower:", greeting.lower())      # Ubah ke huruf kecil semua
print("Title:", greeting.title())      # Huruf kapital di awal setiap kata
print("Replace:", greeting.replace("pagi", "siang"))  # Ganti kata
print("Panjang karakter:", len(greeting))             # Panjang string
print()

# 2.1 String Slicing
# String dapat dipotong (slice) dengan sintaks [awal:akhir:langkah]
# Digunakan untuk mengambil sebagian dari teks.
text = "PythonProgramming"
print("2.1 String Slicing:")
print("Teks asli:", text)
print("Karakter ke-0 sampai 5:", text[0:6])       # Python
print("Karakter dari indeks ke-6:", text[6:])     # Programming
print("Karakter dari belakang:", text[-6:])       # mming
print("Karakter tiap 2 langkah:", text[::2])       # Pto rgamn
print()

# 2.2 String Formatting
# F-string dan .format() memungkinkan penyisipan nilai ke dalam string
# dengan mudah dan rapi.
nama = "Andi"
umur = 25
print("2.2 String Formatting:")
print(f"Halo, nama saya {nama} dan saya berumur {umur} tahun.")
print("Halo, nama saya {} dan saya berumur {} tahun.".format(nama, umur))
print()

# 3. Operasi Aritmatika
# Python mendukung operasi matematika dasar dan lanjutan.
angka1 = 10
angka2 = 3
print("3. Operasi Aritmatika:")
print("Angka 1:", angka1)
print("Angka 2:", angka2)
print("Penjumlahan (a + b):", angka1 + angka2)
print("Pengurangan (a - b):", angka1 - angka2)
print("Perkalian (a * b):", angka1 * angka2)
print("Pembagian (a / b):", angka1 / angka2)
print("Pembagian bulat (a // b):", angka1 // angka2)
print("Sisa bagi (a % b):", angka1 % angka2)
print("Pangkat (a ** b):", angka1 ** angka2)
print()

# 3.1 Penggunaan Modul Math
# Modul math menyediakan fungsi matematika tambahan seperti akar, logaritma, dan pembulatan.
import math
angka = 16
print("3.1 Modul Math:")
print("Akar kuadrat:", math.sqrt(angka))
print("Nilai pi:", math.pi)
print("Nilai log(100):", math.log10(100))
print("Pembulatan ke atas:", math.ceil(4.3))
print("Pembulatan ke bawah:", math.floor(4.7))
print()

# 4. User Input dan Casting
# Semua input dari user bertipe string, perlu diubah (cast) ke tipe numerik
# sebelum digunakan dalam perhitungan.
print("4. Input dan Casting:")
nama_input = input("Masukkan nama kamu: ")
umur_input = int(input("Masukkan umur kamu (angka): "))
tinggi_input = float(input("Masukkan tinggi badan kamu (cm): "))
print("Hai", nama_input.title() + "!")
print("Umur kamu:", umur_input, "tahun")
print("Tinggi badan kamu:", tinggi_input, "cm")
print("Tipe data umur:", type(umur_input))
print("Tipe data tinggi:", type(tinggi_input))
print()

# 5. Conditional Statement
# Digunakan untuk membuat keputusan berdasarkan kondisi yang diberikan.
print("5. Conditional Statement:")
nilai = int(input("Masukkan nilai ujianmu: "))
if nilai >= 90:
    print("Grade: A (Sangat Baik)")
elif nilai >= 80:
    print("Grade: B (Baik)")
elif nilai >= 70:
    print("Grade: C (Cukup)")
else:
    print("Grade: D (Perlu belajar lagi)")
print()

# 5.1 Nested Conditional Statement
# Kondisi bersarang (nested) berguna ketika ada keputusan yang bergantung
# pada kondisi sebelumnya.
print("5.1 Nested Conditional Statement:")
umur = int(input("Masukkan umur kamu: "))
if umur >= 18:
    pekerjaan = input("Apakah kamu sudah bekerja? (ya/tidak): ").lower()
    if pekerjaan == "ya":
        print("Kamu adalah orang dewasa yang bekerja.")
    else:
        print("Kamu adalah orang dewasa yang belum bekerja.")
else:
    print("Kamu masih di bawah umur.")
