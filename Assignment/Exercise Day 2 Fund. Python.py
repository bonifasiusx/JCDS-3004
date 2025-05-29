# 1
import math

x = 4
y = 3
z = 2

xyz = math.pow((x+y*z) / (x*y), 2)

# print(xyz)

# 4
# harga_apel = 10000
# harga_jeruk = 15000
# harga_anggur = 20000

# Cast str ke int supaya bisa dicaro total harganya
# input_apel = int(input('Masukkan Jumlah Apel: '))
# input_jeruk = int(input('Masukkan Jumlah Jeruk: '))
# input_anggur = int(input('Masukkan Jumlah Anggur: '))

# print('\nDetail Belanja\n')

# harga_apel = input_apel * harga_apel
# print(f'Apel : {input_apel} x {harga_apel} = {harga_apel}')

# harga_jeruk = input_jeruk * harga_jeruk
# print(f'Jeruk : {input_jeruk} x {harga_jeruk} = {harga_jeruk}')

# harga_anggur = input_anggur * harga_anggur
# print(f'Anggur : {input_anggur} x {harga_anggur} = {harga_anggur}')

# total_harga = harga_apel + harga_jeruk + harga_anggur
# print(f'\nTotal : {total_harga}') 

# 5
# angka = int(input('Masukkan angka: ')) # Cast dari str ke int supaya bisa dicari kuadratnya

# print(f'Angka kuadrat dari {angka} adalah {angka**2}')

# 6
mesin_A = 5000
mesin_B = 7500
mesin_C = 3500

# Jumlah mesin di pabrik Batam dan Jakarta
batam = (5 * mesin_A) + (2 * mesin_B)
jakarta = (3 * mesin_B) + (7 * mesin_C)

# Durasi lama mesin bekerja memproduksi permen
jam_kerja = 7
hari_kerja = 25

# Kalkulasi hasil
hasil_pabrik_batam = batam * jam_kerja * hari_kerja
hasil_pabrik_jakarta = jakarta * jam_kerja * hari_kerja

total_hasil = hasil_pabrik_batam + hasil_pabrik_jakarta
print(f'Hasil pabrik permen kristal di Batam dan Jakarta selama 1 bulan adalah {total_hasil} permen')
