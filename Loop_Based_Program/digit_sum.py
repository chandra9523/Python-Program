#Find the sum of digit of a number

num = (input("Enter number ="))

sum = 0
for i in num:
    sum = sum +int(i)

print(f"sum of {num} each digit is {sum}")
