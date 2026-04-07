# Print Series 2 4 6 8 ...N
n = int(input("Enter the number upto which even number is required:"))

for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end = ' ')
