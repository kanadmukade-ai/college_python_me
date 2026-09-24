n = int(input("Enter a number: "))

smallest = 1

for i in range(1, n + 1):
    if i < smallest:
        smallest = i

print("Smallest number =", smallest)
