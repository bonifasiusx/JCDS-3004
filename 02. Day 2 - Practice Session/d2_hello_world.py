# This is a simple Python script that prints "Hello World!" and some variables.
print("Hello World!")

nama = 'Joko Minto'
alias = 'Joko Widodo'

print(nama)
print(alias)

# Variable dengan value yang 'masih' kosong
rakPialaArsenal = None

# angka eksponensial
print(123e5)
print(123e-3)

# math Module -> Built-in module for mathematical operations
import math
# Rounds a number to the nearest integer
print(math.ceil(1.4))  # Rounds up
# Returns absolute value of a number
print(math.fabs(-10))  # fabs = float absolute
# Returns the power of a number
print(math.pow(2, 3))  # Returns 8.0 (2 raised to the power of 3)
# Returns the square root of a number
print(math.sqrt(16))  # Returns 4.0
# Returns the value of pi
print(math.pi)  # Returns 3.141592653589793

# Escape characters
print("Hello, I'm Joko Minto")  # Using single quotes inside double quotes
print('Hello, I\'m Joko Minto')  # Using backslash to escape single quote
# tab -> \t
# backspace -> \b 
# new line -> \n

# String Methods
x = 'Halo Dunia'
split_x = x.split(' ') # Hasil split_x akan menjadi list ['Halo', 'Dunia']
index_x = x.index('Dunia')  # Returns the index of 'Dunia' in the string 

# Format Strings
print('Nama saya {}, alias {}, saya berumur {} tahun'.format(nama, alias, 34))