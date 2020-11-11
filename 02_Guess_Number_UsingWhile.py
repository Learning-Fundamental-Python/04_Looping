"""
write a program that randomly generates an integer between 0 and 100, inclusive
The program prompts the user to enter numbers continuously until it matches
the randomly generated number. For each user input, the program reports
whether it is too low or too high, so the user can choose the next input intelligently.
"""
import random

# Generate a random number to be guessed
number = random.randint(0, 100)

print('Guess a magic number between 0 and 100')

# Prompt the user to enter a guess number
guess = -1       # initial value

while guess != number:
    # Prompt user to enter again the guess number
    guess = eval(input('Enter your guess number : '))

    if guess == number:
        print('Yes, the number is', number)
    elif guess > number:
        print('Your guess number too high')
    else:
        print('Your guess number too low')
