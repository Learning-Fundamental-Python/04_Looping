# Write a programs to display prime numbers between 2 and 1,000

count = 0
cout_per_lines = 5

for i in range(2, 100):
    prima = 1
    for j in range(2, i):
        if i % j == 0:
            prima = 0

    if prima == 1:
        count += 1
        print(i, end=' ')
        if count % cout_per_lines == 0:
            print()
