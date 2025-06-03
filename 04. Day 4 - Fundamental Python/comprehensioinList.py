# ==========================================================
# Comprehension List Review
# ==========================================================

# 1. TODO: Buat list berisi angka genap dari 1 sampai 20
list_angka = []

for angka in range(21):
    if angka % 2 == 0:
        list_angka.append(angka)
        
print(f'Hasil: {list_angka}')
#    Contoh hasil: [2, 4, 6, ..., 20]



# 2. TODO: Buat list berisi kata-kata dalam huruf kapital dari list `words`
print()
words = ["list", "comprehension", "in", "python"]

words_result = [] # List baru untuk hasil

for word in words: # For loop untuk setiap kata dari list words
    word = word.upper() # Ubah setiap huruf jadi kapital
    words_result.append(word) # Tambahkan huruf kapital kedalam list hasil
    
print(words_result)
#    Contoh hasil: ["LIST", "COMPREHENSION", "IN", "PYTHON"]



# 3. TODO: Buat list berisi label "genap" atau "ganjil" untuk angka 1 sampai 10
#    Contoh hasil: ["ganjil", "genap", "ganjil", ..., "genap"]

hasil = []

for i in range(1,11): # Stop di 11 supaya angka 10 tidak dilewati
    if i % 2 == 0:
        hasil.append('genap')
    else:
        hasil.append('ganjil')
        
print(f'Hasil: {hasil}')