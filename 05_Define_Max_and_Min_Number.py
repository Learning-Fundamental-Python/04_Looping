"""
Write a program to display max or min number from lines of number
"""
print('Example 01 :')
# Define a maximum number
number = eval(input('Enter an integer : '))
max = number

while number != 0:
    number = eval(input('Enter an integer : '))
    if number > max:
        max = number

print(f"The Maximum number is {max}")


print('\nExample 02 :')
# Define a minimum number
number = eval(input('Enter an integer : '))
min = number

while number != 0:
    number = eval(input('Enter an integer : '))
    if number < min:
        min = number

print(f"The minimum number is {min}")
