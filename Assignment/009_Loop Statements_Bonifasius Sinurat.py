# 1
print('No. 1')
print('======')

spam = 'ababaababbbbcccbabcc'
word = 'bab'

appeared = 0

for i in range(len(spam) - len(word) + 1):
    if spam[i : i + len(word)] == word:
    # Tidak pakai break karena ingin {word} muncul secara total di {spam}
        appeared += 1
print(f'Appeared {appeared} times')

# 2
print()
print('No. 2')
print('======')

# Pake function input() & .lower() untuk menguji peka huruf besar-kecil
spam2 = input('Input: ')

huruf_o = 0
huruf_x = 0

# Cek setiap huruf dari input user di spam2
for huruf in spam2:
    if huruf.lower() == 'o':
        huruf_o += 1
    elif huruf.lower() == 'x':
        huruf_x += 1

# Hitung setiap huruf 'o' dan 'x' yang terdeteksi
if huruf_o == huruf_x and (huruf_o + huruf_x) > 0:
    print(True)
else:
    print(False)

# 3
print()
print('No. 3')
print('======')

number = input('Enter number: ')

narcissistic_result = 0

for n in number: # Number tetep str biar bisa make len()
    narcissistic_result += int(n) ** len(number) # Setiap digit ** len(angka yang di-input oleh user)
if narcissistic_result == int(number):
    # Jika hasil sama dengan angka yang user input -> narcissistic
    print(f'{number} is narcissistic number')
else:
    # Cek ulang dengan input angka-angka lainnya
    print(f'{number} is NOT narcissistic number')
            
# 4
print()
print('No. 4')
print('======')

fullname = input('Name: ')
name = fullname.split() # Pisahkan setiap kata

# Ambil Inisial di kata pertama dan terakhir
first_letter = name[0][0]
last_letter = name[-1][0]

print(f'{first_letter.upper()}.{last_letter.upper()}')

# 5
print()
print('No. 5')
print('======')

input_angka = input('Masukkan angka: ')

angka_faktorial = int(input_angka)

# Untuk setiap angka dari range(misal input: 5), 5 * (5-1) -> 20 * (4-1), dst
for angka in range(angka_faktorial, 1, -1):
    angka_faktorial *= (angka - 1)

# Cek hasil angka_faktorial == Genap    
if angka_faktorial % 2 == 0:
    print(f'{int(input_angka)}! = {angka_faktorial}')