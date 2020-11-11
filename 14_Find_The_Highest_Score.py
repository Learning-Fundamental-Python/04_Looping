# Write a programs to find the highest score

# Prompt user to input score of students
amount_of_students = eval(input("Enter the number of your students : "))
highest_score = eval(input("Enter the score of your students : "))

for i in range(1, amount_of_students):
    your_score = eval(input("Enter your score : "))

    score = your_score

    if score > highest_score:
        highest_score = score

# Display the result
print(f"The highest score is {highest_score}")
