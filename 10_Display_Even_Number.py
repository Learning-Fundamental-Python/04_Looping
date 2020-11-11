# Write a program to display lines of even numbers
number = 0
count = 0

print('Deret Bilangan Genap : ')

while number <= 10:
    if number % 2 == 0:
        genap = number
        print(genap, end=' ')
        count = count + 1

    number = number + 1

print(f"\nJumlah bilangan genap : {count}")
