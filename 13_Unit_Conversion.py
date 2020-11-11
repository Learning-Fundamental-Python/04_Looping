# Write a program to conversion each of units
import math

print('Example 01 :')
# Conversion from kilograms to pounds
print(f"Kilograms\t Pounds")
for kilograms in range(1, 201, 2):
    pounds = kilograms * 2.2

    print(f"{kilograms:5.0f} {pounds:12.2f}")

print('\nExample 02:')
# Conversion from miles to kilometers
print('Miles\t\t Kilometers')
for miles in range(1, 11):
    kilometers = miles * 1.609
    print(f"{miles:3.0f} {kilometers:16.2f}")

print('\nExample 03 :')
print(f"Kilograms\t Pounds\t   |   \tPounds\t Kilograms")
kilograms = 1
pounds = 20
while kilograms <= 199 and pounds <= 515:
    pd = kilograms * 2.2
    kg = pounds * 0.45

    print(f"{kilograms:5.0f} {pd:13.2f} {pounds:12.0f} {kg:11.2f}")

    kilograms += 2
    pounds += 5

print('\nExample 04 :')
print(f"Miles\t Kilometers\t   |   \tKilometers\t Miles")
miles = 1
kilometers = 20

while miles <= 10 and kilometers <= 65:
    km = miles * 1.609
    ml = kilometers * 0.621

    print(f"{miles:3.0f} {km:12.2f} {kilometers:15.0f} {ml:13.2f}")

    miles += 1
    kilometers += 5

print('\nExample 05 :')
print(f"Degree\t\t Sin\t\t Cos")
# display the sin value and cos value of degrees
# from 0 to 360 with increments of 10 degrees.

for radian in range(0, 370, 10):
    sinus = math.sin(math.radians(radian))
    cosinus = math.cos(math.radians(radian))

    print(f"{radian:3.0f} {sinus:14.4f} {cosinus:11.4f}")
