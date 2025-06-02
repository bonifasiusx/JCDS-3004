x = None
print(bool(x) == False)

pemohonSIM = []

# While true bisa digunakan untuk kondisi countable dan uncountable juga
while True: # Pake while karena user input -> uncountable condition
    dataPemohon = input('Masukkan umur Anda: ')
    if dataPemohon.lower() == 'selesai':
        break
    else:
        pemohonSIM.append(dataPemohon)

print('Data pemohon SIM', pemohonSIM)

# For loop
for umur in pemohonSIM:
    print(umur)
    
# For loop angka menurun
for i in range(10, 0, -1): # Step -1 jadi i -> menurun
    print(i)

# Continue berguna untuk melewati (meng-skip) sebuah task di dalam loop
