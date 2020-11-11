####################################
# Using Keyword Break and Continue
# for Looping
####################################
# The break and continue keywords provide -
# additional controls to a loop.

print("Example 1 :")
# Use keyword break for looping
sum = 0
number = 0

while number < 20:
    number += 1
    sum += number
    if sum >= 100:
        break
    print(sum, end=' ')

# Display the result
print(f"\nThe number is {number}")
print(f"The sum is {sum}")

print("\nExample 2 :")
# Use keyword continue for looping
sum = 0
number = 0

while number < 20:
    number += 1
    if number == 10 or number == 11:
        continue
    sum += number

# Display the result
print(f"The sum is {sum}")

print("\nExample 3 :")
n = eval(input("Enter an integer >= 2 : "))
factor = 2

while factor <= n:
    if n % factor == 0:
        break
    factor += 1

# Display the result
print(f"The smallest factor other than 1 for {n} is {factor}")

print("\nExample 3b :")
# rewrite the code 'Example 2' without using break

n = eval(input("Enter an integer >= 2 : "))
factor = 2

# using boolean operator
found = False

while (factor <= n) and (not found):
    if n % factor == 0:
        found = True
    else:
        factor = factor + 1

# Display the result
print(f"The smallest factor other than 1 for {n} is {factor}")

print("\nExample 4 :")
balance = 20

while True:
    if balance < 9:
        break
    print(balance)
    balance = balance - 9

# Display the result
print(f"Balance is {balance}")

print("\nExample 4b :")
balance = 100

while True:
    if balance < 9:
        continue
    balance = balance - 9

print("Balance is", balance)

print("\nExample 5 :")
# Convert FOR Loop into WHILE Loop
# FOR Looping
sum = 0

for i in range(4):
    if i % 3 == 0:
        continue
    sum = sum + i

print(f"The sum is {sum}")

# WHILE Looping
sum = 0
i = 1

while i < 4:
    if i % 3 == 0:
        break
    sum = sum + i
    i = i + 1

print(f"The sum is {sum}")

print("\nExample 5b :")
# WHILE Looping
i = 0
while i <= 10:
    i = i + 1
    if i > 5:
        break

    print(i)

print("\nExample 6 :")
# Rewrite Example 1 dan Example 2 without-
# using break and continue statements

print("Example 6a :")
sum = 0
number = 0
result = False

while number < 20 and not result:
    number = number + 1
    sum = sum + number
    if sum >= 100:
        result = True

print("The number is", number)
print("The sum is", sum)

print("\nExample 6b :")
sum = 0
number = 0

result = False

while number < 20 and not result:
    number = number + 1
    sum = sum + number

    if number == 10 or number == 11:
        result = True

print("The number is", number)
print("The sum is", sum)

print("\nExample 7 :")
for i in range(1, 4):
    for j in range(1, 4):
        if i * j > 2:
            break

        print(i * j)

    print(i)

print("\nExample 7b :")
for i in range(1, 4):
    for j in range(1, 4):
        if i * j > 2:
            continue

        print(i * j)

    print(i)

print("\nExample 7c :")
for i in range(1, 10):
    if i < 5:
        break
    print(i)

    print((i * 2))

print("\nExample 7d :")
for i in range(1, 10):
    if i < 5:
        continue
    print(i)

    print((i * 2))

print("\nExample 8 :")
# Displaying Prime Numbers
'''
This section presents a program that displays the first-
fifty prime numbers in five lines, each containing ten numbers.
'''
# Prime Numbers is An integer greater than 1 and
# if its only positive divisor is 1 or itself.
NUMBER_OF_PRIMES = 50  # Number of primes to display
NUMBER_OF_PRIMES_PER_LINE = 10  # Display 10 per line
count = 0  # Count the number of prime numbers
number = 2  # A number to be tested for primeness

print("The first 50 prime numbers are : ")

# Repeatedly find prime numbers
while count < NUMBER_OF_PRIMES:
    # Assume the number is prime
    is_prime = True  # is the current number prime

    # Test if number is prime
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # if true, the number is not prime
            is_prime = False  # set is_prime to false
            break  # Exit for the loop
        divisor = divisor + 1

    # Display the prime number and increase the count
    if is_prime:
        count = count + 1  # Increase the count

        print(format(number, "5d"), end=' ')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # Display the prime number and increase the count
            print()  # Jump to the new line

    # Check if the next number is prime
    number = number + 1
