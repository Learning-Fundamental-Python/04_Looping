"""
Write a program to count positive and negative numbers
and compute the average of numbers
"""
number = 1
positive = 0
negative = 0
count = 0
sum = 0
average = 0
count2 = 0

while number != 0:
    number = eval(input('Enter an integer, the input ends if it is 0: '))
    count += 1

    if number > 0:
        positive = positive + 1
    if number < 0:
        negative = negative + 1

    average = sum / count
    sum = sum + number

print(f"The number of positives is {positive}")
print(f"The number of negatives is {negative}")
print(f"The total number is {sum}")
print(f"The average is {average}")
