#write a program to check whether a number is 3 digit number or not

num = (input("Enter a number :"))
count = len(num)
if count == 3:
    print(f"{num} is {count} digit number")
else:
    print(f"{num} is not 3 digit number ")