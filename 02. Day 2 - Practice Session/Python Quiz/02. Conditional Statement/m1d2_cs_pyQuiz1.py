# Buat Program untuk menghitung IMT (Index Massa Tubuh)

# Tentang IMT
# Indeks Massa Tubuh (IMT) adalah alat skrining yang banyak digunakan untuk 
# menilai berat badan seseorang dalam kaitannya dengan tinggi badannya.

# Cara menghitung IMT
# berat(kg) / (tinggi(m) ^ 2)

# Klasifikasi IMT
# < 18,5 = Kekurangan Berat Badan
# 18,5 - 24,9 = Normal
# 25 - 29,9 = Berat Badan Berlebih
# > 30 = Obesitas

# Spesifikasi program
# input: tinggi_badan, berat_badan
# output: klasifikasi IMT dan kalkulasi IMT

tinggi_badan = int(input('Masukkan tinggi badan Anda (CM): '))
berat_badan = float(input('Masukkan berat badan Anda (KG): '))

tinggi_badan_m = tinggi_badan / 100
kalkulasi_IMT = berat_badan / tinggi_badan_m^2

if kalkulasi_IMT < 18.5:
    print('Kekurangan Berat Badan')
elif kalkulasi_IMT >= 18.5 and kalkulasi_IMT < 25:
    print('Normal')
elif kalkulasi_IMT >= 25 and kalkulasi_IMT < 30:
    print('Berat Badan Berlebih')
else:
    print('Obesitas')
    
