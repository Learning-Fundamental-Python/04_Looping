# Write a programs to display any pattern of looping
###########################################

print('Example 1 :')
for i in range(1, 7, 1):
    for j in range(1, i + 1, 1):
        print('*', end=' ')
    print()

print('\nExample 2 :')
for i in range(7, 1, -1):
    for j in range(i - 1, 0, -1):
        print('*', end=' ')
    print()

print('\nExample 3a :')
maks = 6
limit = maks
for star in range(0, maks, 1):
    for pattern in range(0, star, 1):
        print(pattern, end=' ')

    for form in range(0, limit):
        print('*', end=' ')

    limit -= 1
    print(" ")

print('\nExample 3b :')
maks = 6
limit = maks
for star in range(0, maks):
    for pattern in range(0, star):
        print(' ', end=' ')

    for form in range(0, limit):
        print("*", end=' ')
    limit -= 1
    print()

print('\nExample 3c :')
maks = 6
limit = maks
for star in range(0, maks):
    for pattern in range(0, limit + 1):
        print(" ", end=' ')

    for form in range(0, star + 1):
        print('*', end=' ')

    limit -= 1
    print()

print('\nExample 3d :')
maks = 6
limit = maks
for star in range(0, maks):
    for pattern in range(0, limit + 1):
        print(" ", end='')

    for form in range(0, star + 1):
        print('*', end=' ')

    limit -= 1
    print()

print('\nExample 3e :')
maks = 6
limit = maks
for star in range(0, maks):
    for pattern in range(0, star):
        print(' ', end='')

    for form in range(0, limit):
        print("*", end=' ')
    limit -= 1
    print()

print('\nExample 3f :')
maks = 6
limit = maks
for star in range(1, maks):
    for pattern in range(0, star):
        print(' ', end='')

    for form in range(0, limit):
        print("*", end=' ')
    limit -= 1
    print()

maks = 6
limit = maks
for star in range(0, maks):
    for pattern in range(1, limit + 1):
        print("", end=' ')

    for form in range(0, star + 1):
        print('*', end=' ')

    limit -= 1
    print()
