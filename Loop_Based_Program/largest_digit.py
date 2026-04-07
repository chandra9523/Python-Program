#find the largest digit in a number

num = (input("Enter a number:"))

large = float('-inf')

for i in num:
    if int(i) > large:
        large = int(i)

print(large)