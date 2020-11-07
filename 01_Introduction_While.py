#################################################
# Introduction WHILE - Looping In Python Program
#################################################
import random
import time

# The While loop
'''
The while loop is a condition-controlled loop; it is
controlled by a "true/false" condition.
'''

print("Example 01 :")
# Display text as much as 20 times
count = 0
while count < 20:
    print("I Love Python Programming!...")
    count = count + 1

print("\nExample 02 :")
# gives a program that prompts the user to enter an answer for a question on subtraction.

# Generate two random single-digit integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# if number1 < number2, swap number1 with number2
if number1 < number2:
    number1, number2 = number2, number1

# Prompt the user to answer "what number1 - number2?"
answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

# Repeatedly ask the question until the answer is correct
while number1 - number2 != answer:
    answer = eval(input("Wrong Answer!...Please Try Again. What is "
                        + str(number1) + " - " + str(number2) + "? "))

print("You Got it!...")

print("\nExample 03 :")
'''
The program prompts the user to enter numbers continuously 
until it matches the randomly generated number.
'''

# Generate a random number to be guessed
number = random.randint(0, 100)

print("Guess a magic number between 0 and 100")

# Prompt the user to enter a guess number
guess = -1  # initial value

while guess != number:
    # Prompt user to enter again the guess number
    guess = eval(input("Enter your guess number : "))

    if guess == number:
        print("Yes, the number is", number)
    elif guess > number:
        print("Your guess number too high")
    else:
        print("Your guess number too low")

print("\nExample 4 :")
# Multiple Subtraction Quiz

correct_count = 0  # Count the number of correct answer
count = 0  # count the number of question
NUMBER_OF_QUESTIONS = 5  # Make a Constant

start_time = time.time()  # Get start time

while count < NUMBER_OF_QUESTIONS:
    # Generate two random single-digit integers
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    # if number1 < number2, swap number1 with number2
    if number1 < number2:
        number1, number2 = number2, number1

    # Prompt the user to answer "What is number1 - number2 ?"
    answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

    # Grade the answer and display the result
    if number1 - number2 == answer:
        print("You are correct!...")
        correct_count += 1
    else:
        print("You answer wrong!...\n", number1, "-", number2, "is", number1 - number2)

    # Increase the count
    count += 1

end_time = time.time()  # Get the end time of quiz
test_time = format((end_time - start_time), ".0f")  # Get the test time

print(f"Correct count is {correct_count} out of {NUMBER_OF_QUESTIONS}")
print(f"Test time is {test_time} seconds")

print("\nExample 5 :")
# Controlling a Loop with a Sentinel Value
data = eval(input("Enter an integer (the input ends " +
                  "if it is 0) : "))

# keep reading data until the input is 0
sum = 0
while data != 0:
    sum += data

    data = eval(input("Enter an integer (the input ends " +
                      "if it is 0) : "))

print(f"The sum is {sum}")

print("\nExample 6 :")
print("Example 6a :")
i = 1
while i < 10:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1  # diletakkan sesuai identasi pada WHILE bukan IF

print("Example 6b :")
i = 1
while i < 10:
    if 1 % 2 == 0:
        print(i)
        i = i + 1  # tidak muncul jawaban karena identasi pada IF bukan WHILE

print("\nExample 7 :")
count = 0
while count < 10:
    print(count, end=' ')
    count += 1

print("\nExample 8 :")
# Define a maximum number
number = eval(input("Enter an integer : "))
max = number

while number != 0:
    number = eval(input("Enter an integer : "))
    if number > max:
        max = number

print(f"Max is {max}")
print(f"number is {number}")

print("\nExample 8b :")
# Define a minimum number
number = eval(input("Enter an integer : "))
min = number

while number != 0:
    number = eval(input("Enter an integer : "))
    if number < min:
        min = number

print(f"The minimum number is {min}")
print(f"The number is {number}")
