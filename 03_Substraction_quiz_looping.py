"""
Write a program that generates five questions and, after a student answers all of
them, reports the number of correct answers.
The program also displays the time spent on the test.
"""
import random
import time

print('Multiple Subtraction Quiz :')

correct_count = 0           # Count the number of correct answer
count = 0                   # count the number of question
NUMBER_OF_QUESTIONS = 5     # Make a Constant

start_time = time.time()    # Get start time

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

end_time = time.time()                                     # Get the end time of quiz
test_time = format((end_time - start_time), ".0f")         # Get the test time

print(f"Correct count is {correct_count} out of {NUMBER_OF_QUESTIONS}")
print(f"Test time is {test_time} seconds")
