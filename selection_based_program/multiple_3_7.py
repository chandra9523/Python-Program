#write a python program to check whether number if multiple of 3 or 7

num = int(input("Enter a Number:"))

if (num % 3 == 0 or num % 7 == 0):
    print(f"{num} is multiple of 3 or 7")
else:
    print(f"{num} is not multiple of 3 or 7")