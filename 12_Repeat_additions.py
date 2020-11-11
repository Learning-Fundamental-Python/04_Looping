"""
Revise the program to generate ten random addition questions for
two integers between 1 and 15.
Display the correct count and test time.
"""
import random
import time
correct_count = 0
total_questions = 1

start_time = time.time()    # Get start time

for total_questions in range(1, 11):
    number1 = random.randint(1, 15)
    number2 = random.randint(1, 15)

    count = eval(input(f"{number1} + {number2} = "))

    if number1 + number2 == count:
        print("You get correct answer!...")
        correct_count += 1
    else:
        print("You get wrong answer!...")

end_time = time.time()                      # Get end time
test_time = int(end_time - start_time)      # Get test time

print(f"\nYou get test time in {test_time} seconds")
print(f"Total correct answer : {correct_count}")
print(f"You get {correct_count} correct answer of "
      f" {total_questions} questions")
