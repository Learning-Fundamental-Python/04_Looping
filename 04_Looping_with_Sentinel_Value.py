"""
Write a programs that can reads and calculates
the sum of an unspecified number of integers.
The input 0 signifies the end of the input.
"""
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
