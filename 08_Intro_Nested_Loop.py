############################################
# Introduction Nested Loops
# A loop can be nested inside another loop
############################################
import random
"""
Nested loops consist of an outer loop and one or more inner loops. Each time the outer loop is
repeated, the inner loops are reentered and started a new.
"""

# Nested FOR Looping
print("Example 1 :")
print("Multiplication Table")
# Display the number title
print("  |", end='')
for j in range(1, 10):
    print("  ", j, end='')
print()
print("-----------------------------------------")

# Display table body
for i in range(1, 10):
    print(i, "|", end='')
    for j in range(1, 10):
        # Display the product and align properly
        print(format(i * j, "4d"), end='')
    print()

print("\nExample 2a :")
j = 0
while j < 5:
    print(j, end=' ')
    j = j + 1

print("\nExample 2b :")
for i in range(1, 3):
    print(i)
    # print(i)
    j = 0
    while j < i:
        j = j + 1
        print(j, end=' ')

print("\nExample 2c :")
for i in range(1, 5):
    print(i)
    j = 0
    while j < i:
        print(j, end=' ')
        j = j + 1

print("\nExample 2d :")
for i in range(1, 5):
    print('*')
    j = 0
    while j < i:
        print(j)
        j = j + 1

print("\nExample 2e :")
for i in range(4):
    for j in range(4):
        print([], end=' ')
    print()                 # newline

print("\nExample 2f :")
for i in range(3):
    for j in range(4):
        print('*', end=' ')
    print()

print("\nExample 2g :")
for i in range(6):
    j = 0
    while j < i:
        j = j + 1
        print(j, end=' ')
    print()

print("\nExample 2h :")
for i in range(5, 0, -1):
    j = 0
    while j < i:
        j = j + 1
        print(j, end=' ')
    print()

print("\nExample 2i :")
for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print()

print("\nExample 2j :")
for i in range(5):
    for j in range(5):
        print(j, end=' ')
    print()

print("\nExample 2k :")
for i in range(5):
    for j in range(5):
        if j % 2 == 0:
            print('*', end=' ')
        else:
            print('_', end=' ')
    print()

print("\nExample 2l :")
i = 0
while i < 5:
    for j in range(i, 1, -1):
        print(j, end=' ')
    print('****')
    i = i + 1

print("\nExample 2m :")
i = 5
while i >= 1:
    num = 1
    for j in range(1, i + 1):
        print(num, end="xxx")
        num = num * 2
    print()
    i = i - 1

print("\nExample 2n :")
i = 1
while i <= 5:
    num = 1
    for j in range(1, i + 1):
        print(num, end="G ")
        num = num + 2
    print()
    i = i + 1

print("\nExample 3 :")
# Using floating-point numbers in the loop-
# continuation-condition may cause numeric errors.

# Initialize sum
sum = 0

# add 0.01, 0.02, ...., 0.09, 1 to sum
i = 0.01
while i <= 1.0:
    sum = sum + i
    i = i + 0.01

# Display result
print(f"The sum is {sum:.2f}")

print("\nExample 4 :")
# presents a program that prompts the user to-
# enter two positive integers and finds their-
# greatest common divisor

# Prompt the user to enter two integer
n1 = eval(input("Enter first integer : "))
n2 = eval(input("Enter second integer : "))

# initially variable
gcd = 1
k = 1

while k < n1 and k < n2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k = k + 1

# Display the result
print(f"The greatest common divisor for {n1} and {n2} is {gcd}")

print("\nExample 4b :")
# presents a program that prompts the user to-
# enter two positive integers and finds their-
# greatest common divisor

# Prompt the user to enter two integer
n1 = eval(input("Enter first integer : "))
n2 = eval(input("Enter second integer : "))

# initially variable
gcd = 1
k = 1

while k < n1 // 2 and k < n2 // 2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k = k + 1

# Display the result
print(f"The greatest common divisor for {n1} and {n2} is {gcd}")

print("\nExample 5 :")
# Predicting the Future Tuition
year = 0            # Year 0
tuition = eval(input("Enter Your first tuition : "))   # Year 1
increase_tuition = tuition * 2

while tuition < increase_tuition:
    year = year + 1
    tuition = tuition * 1.07

# Display the result
print(f"The tuition will be doubled in {year} years")
print(f"The tuition will ${tuition:.2f} in {year} years")

print("\nExample 6 :")
NUMBER_OF_TRIALS = 10000    # Constant
number_of_hits = 0

for i in range(NUMBER_OF_TRIALS):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1

    if (x * x + y * y) <= 1:
        number_of_hits += 1

pi = 4 * number_of_hits / NUMBER_OF_TRIALS

print(f"PI is {pi}")
