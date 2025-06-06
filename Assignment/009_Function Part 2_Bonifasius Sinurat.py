# 1
print('No. 1')
print('=====')
# Kemarin kita sudah membuat program faktorial menggunakan for loop. Kali ini, buatlah program faktorial menggunakan fungsi rekursif.

# Constraint:
# Fungsi memiliki input dan output.
# Terdapat proses rekursif.
# Beri nama fungsi tersebut dengan `fact()`

# Case
# print ( fact(3) )

# Output:
# 6

def fact(n):
    if n == 0 or n == 1: # Kondisi berhenti
        return 1
    else:
        return n * fact(n-1) # Recursive
print(fact(5))

# 2
print()
print('No. 2')
print('=====')
# Buat sebuah function yang akan menerima 1 argument dengan tipe data list, dimana semua data didalam listnya akan memiliki tipe data integer. 

# Kemudian, function tersebut akan mengembalikan value ke pemanggilnya berupa sebuah list yang berisikan tipe data string semua, dimana functionnya hanya akan merubah setiap angka yang terdapat didalam list, ke kategori angkanya masing2, baik itu dia angka ganjil atau angka genap.

# Untuk hintnya, teman2 dapat menggunakan map function dari Python untuk melakukan ini.
list1 = [1,3,4,5]
list2 = [22,17,19,20,14]
list3 = [1,3,5]
list4 = [2,4,6]

# Fungsi biasa
def cekGanjilGenap(angka):
    if angka % 2 != 0:
        return 'Ganjil'
    else:
        return 'Genap'
hasilMap = list(map(cekGanjilGenap, list1))   
print(hasilMap)
print()

# Lambda
mapList = list(map(lambda angka: 'Ganjil' if angka % 2 != 0 else 'Genap', list1))
print(mapList)

# 3
print()
print('No. 3')
print('=====')
# Buat sebuah function yang dapat melakukan filtering terhadap list gaji yang berisikan 5 data ini. Carilah data gaji yang akan tetap bernilai diatas 9jt setelah dikurangi 5% dari nilai gaji tersebut. Berarti dari kelima data gaji pada list tersebut, hanya akan tersisa tiga data saja. Dimana hanya 3 data saja dari 5 data pada list tersebut yang akan lebih besar dari 9jt setelah dikurangi Tapera 5% dari nominal gajinya.

# Untuk hint nya, teman2 dapat menggunakan filter function dari Python untuk melakukan ini.
listGaji = [9100000, 9800000, 9500000, 10300000, 9300000]

# Fungsi biasa
def filterGaji(manaGaji):
    manaGaji -= (manaGaji * 5 / 100)
    if manaGaji >= 9000000:
        return manaGaji
    else:
        return
filteredGaji = list(filter(filterGaji, listGaji))
print(filteredGaji)
print()

# Lambda
lambdaFilteredGaji = list(filter(lambda gaji: gaji - (gaji * 0.05) >= 9000000, listGaji))
print(lambdaFilteredGaji)