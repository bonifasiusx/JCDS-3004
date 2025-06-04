# 1
print('No. 1')
print('=====')

def avg(list1):
    total = sum(i for i in list1) # Jumlahkan setiap i
    panjang = len(list1)
    return total / panjang # Cari rata-rata

list = [5, 6, 3, -1, -3, 5]
print(avg(list))

# 2
print()
print('No. 2')
print('=====')

def gcd(a,b):
    if a <= 0 or b <= 0: # Constraint 0 dan bilangan negatif
        print('Input cannot be zero or negative')
        return # -> Break
 
    faktor = 1 # Bilangan positif
    for i in range(1, (a+b) + 1): # (a+b) -> cari angka paling tinggi
        if a % i == 0 and b % i == 0: # Pake 'and' bukan 'or'
            faktor = i
    
    if faktor == 1: # Kondisi coprime
        print(f'{a} and {b} are coprime number')
        return # -> Break
    else:
        return faktor # Tampilkan {faktor} di terminal

print(gcd(15, 25))  # 5
print(gcd(9, 7))    # "9 and 7 are coprime number"
print(gcd(0, 1))    # "Input cannot be zero or negative"

# 3
print()
print('No. 3')
print('=====')

def isLeapYear(year):
    # Modulus dari paling besar ke paling kecil
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(isLeapYear(1999)) # False
print(isLeapYear(2000)) # True
print(isLeapYear(2001)) # False
print(isLeapYear(2004)) # True
print(isLeapYear(2100)) # False
print(isLeapYear(2400)) # True
