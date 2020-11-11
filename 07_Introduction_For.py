#################################################
# Introduction FOR - Looping In Python Program
#################################################

print('Example 1 :')
# For Looping
for i in range(5):
    print(i)

print('\nExample 2 :')
# While Looping
i = 0

while i < 5:
    print(i)
    i = i + 1

print('\nExample 3 :')
# Looping - FOR
# Suppose the input is 2 3 4 5 0 (one number per line)
number = 0
sum = 0

# Define the output based on input
for count in range(5):
    number = eval(input('Enter an integer : '))
    sum = sum + number

print(f'sum is {sum}')
print(f'The count is {count}')

print('\nExample 04 :')
# For Looping
sum = 0
for i in range(20):
    sum = sum + i
    print(i, end=' ')

print(f"\nsum is {sum}\n")

print('\nExample 05 :')
# Looping FOR in string
nama_kota = 'Siantar'
for huruf in nama_kota:
    print(huruf)
print()

# WHILE Looping in string
nama_kota = 'Siantar'
i = 0

while i < len(nama_kota):
    huruf = nama_kota[i]
    print(huruf)
    i = i + 1

print('\nExample 06 :')
# Menampilkan deret bilangan berpola tertentu
for i in range(0, 10):
    print(i, end=' ')
print()

for i in range(0, 10, 2):
    print(i, end=' ')
print()

for i in range(1, 10, 2):
    print(i, end=' ')
print()

for i in range(10):
    print(i, end=' ')
print()

for i in range(10):
    print("Halo!...", end=' ')
print()

for i in range(10, 0, -1):
    print(i, end=' ')

print('\nExample 07 :')
# Program ini menampilkan sebuah tabel yang menunjukkan pertumbuhan investasi

# mendefinisikan tiap konstanta
SUKU = 5.0
SALDO_AWAL = 10000

# Membaca banyak tahun untuk perhitungan
banyak_tahun = eval(input('Masukkan banyak tahun : '))

# Menampilkan tabel dari saldo untuk tiap tahunnya
saldo = SALDO_AWAL
for tahun in range(1, banyak_tahun + 1):
    bunga = saldo * SUKU / 100
    saldo = saldo + bunga
    print("%4d $%10.2f" % (tahun, saldo))
