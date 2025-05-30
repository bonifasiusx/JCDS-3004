# Repo Link : https://github.com/bonifasiusx/JCDS-3004/tree/main/Assignment

# 1
import math

x = 4
y = 3
z = 2

xyz = math.pow((x+y*z) / (x*y), 2)
# atau xyz = ((x+y*z) / (x*y))**2
print(xyz)

# 2
print()
# Cari umur Andi dan Budi dulu, lalu masing-masing ditambah 2
# Andi (a), Budi (b)
# a + b = 49
# a / b = 0.4

# a = 0.4 * b
# 0.4b + b = 49
# (0.4 + 1)b = 49

b = 49 / 1.4 # = 35 (Umur Budi)
a = 0.4 * b # = 14 (Umur Andi)

print(f'Umur Andi 2 tahun lagi adalah {int(a) + 2}')
print(f'Umur Budi 2 tahun lagi adalah {int(b) + 2}')

# 3
print()
jarak = 120
mobil_A = 60
mobil_B = 40

# Kecepatan mobil A dan B saling mendekat
total_kecepatan = mobil_A + mobil_B
# Mencari waktu tabrakan
waktu = (jarak / total_kecepatan) * 60 # 1.2 x 60 = 72 menit
jam_tabrakan = int(waktu // 60) + 9 # Misal mobil A & B melaju pukul 09:00 WIB
menit_tabrakan = int(waktu) % 60 # Cast dari float ke int supaya jamnya bukan bilangan desimal

# 09:00 + 72 menit (1 jam 12 menit) = 10:12 WIB
print(f'Mobil A dan Mobil B akan bertabrakan pukul {jam_tabrakan}:{menit_tabrakan} WIB.')

# 4
print()
harga_apel = 10000
harga_jeruk = 15000
harga_anggur = 20000

# Cast str ke int supaya bisa dicari total harganya
input_apel = int(input('Masukkan Jumlah Apel : '))
input_jeruk = int(input('Masukkan Jumlah Jeruk : '))
input_anggur = int(input('Masukkan Jumlah Anggur : '))

print('\nDetail Belanja\n')

total_apel = input_apel * harga_apel
print(f'Apel : {input_apel} x {harga_apel} = {total_apel}')

total_jeruk = input_jeruk * harga_jeruk
print(f'Jeruk : {input_jeruk} x {harga_jeruk} = {total_jeruk}')

total_anggur = input_anggur * harga_anggur
print(f'Anggur : {input_anggur} x {harga_anggur} = {total_anggur}')

total_harga = total_apel + total_jeruk + total_anggur
print(f'\nTotal : {total_harga}')

# 10
# Minta uang dari user dan hitung uang dengan total harga belanja
uang = int(input('\nMasukkan jumlah uang : '))
if uang > total_harga: # Jika uang > total_harga, kasih kembalian
    kembalian = uang - total_harga
    print('\nTerima kasih')
    print(f'Uang kembalian Anda : {kembalian}')
elif uang < total_harga: # Jika uang < total_harga, tunjukin kurangnya
    kekurangan = total_harga - uang
    print('\nTransaksi Anda dibatalkan')
    print(f'Uangnya kurang sebesar {kekurangan}')
else: # Kondisi yang tersisa cuma uang == total_harga
    print('\nTerima kasih')
    
# 5
print()
angka = int(input('Masukkan angka: ')) # Cast dari str ke int supaya bisa dicari kuadratnya

print(f'Angka kuadrat dari {angka} adalah {angka**2}')

# 6
print()
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

# 7
print()
tahun = 360
bulan = 30
minggu = 7

# Input angka dari user untuk menghitung hari
hitung_hari = int(input('Masukkan hari yang ingin dihitung: '))

hasil_tahun = hitung_hari // tahun # Misal input 400 --> 400 // 360 = 1 tahun
hasil_bulan = hitung_hari % tahun // bulan # 400 % 360 // 30 = 1 bulan
hasil_minggu = hitung_hari % tahun % bulan // minggu # 400 % 360 % 30 // 7 = 1 minggu 
sisa_hari = hitung_hari % tahun % bulan % minggu

print(f'{hasil_tahun} Tahun {hasil_bulan} Bulan {hasil_minggu} Minggu {sisa_hari} Hari')
# Cek ulang hasil dengan input 550 hari = 1 Tahun 6 Bulan 1 Minggu 3 Hari

# 8
print()
# Minta user masukkan angka dan cast str ke int
cek_angka = int(input('Masukkan angka yang mau dicek: '))

if cek_angka % 2 == 0:
    print(f'Number {cek_angka} is even')
else:
    print(f'Number {cek_angka} is odd')

# 9
print()
massa = int(input('Masukkan Massa (kg): '))
tinggi = int(input('Masukkan Tinggi (cm): '))
tinggi_meter = tinggi / 100
print(f'Massa {massa} kg dan tinggi {tinggi_meter} m')

IMT = massa / (tinggi_meter**2)
# Kondisi IMT
if IMT < 18.5:
    print(f'IMT = {IMT}, BERAT BADAN KURANG!')
elif IMT >= 18.5 and IMT < 25:
    print(f'IMT = {IMT}, BERAT BADAN IDEAL!')
elif IMT >= 25 and IMT < 30:
    print(f'IMT = {IMT}, BERAT BADAN BERLEBIH!')
elif IMT >= 30 and IMT < 40:
    print(f'IMT = {IMT}, BERAT BADAN SANGAT BERLEBIH!')
else:
    print(f'IMT = {IMT}, OBESITAS!')


# ============================================ #
# BONUS ROUND

# 11
print()
n = int(input('Enter number: '))
if n % 2 == 0 and (n >= 2 and n < 5): # Gapake '<= 5' karena 5 itu Ganjil
    print('Not Weird')
elif n % 2 == 0 and (n >= 6 and n <= 20):
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')
else: # Cuma sendiri yang nyari Ganjil jadi taro di Else aja
    print('Weird')

# 12
print()
first_name = input('Enter your name: ')
sur_name = input('Enter your surname: ')

print(f'Hello {first_name} {sur_name}! You just delved into python.')

# 13
print()
kumpulan_kata = 'Marilah seluruh rakyat Indonesia arahkan pandangamu ke depan!'
# Pake method .replace untuk ngeganti spasi dengan simbol strip
pisahkan_kata = kumpulan_kata.replace(' ', '-')
print(pisahkan_kata)

# 14
print()
input_a = int(input('Masukkan a: '))
input_b = int(input('Masukkan b: '))

# Cari output pake // biar dapet int dan % biar dapet sisanya
output_a = input_a // input_b
output_b = input_a % input_b
output_divmodnya = f'({output_a},{output_b})'

print(output_a)
print(output_b)
print(output_divmodnya)