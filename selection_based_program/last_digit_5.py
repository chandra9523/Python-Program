#write a python program to check whether a last digit of a number is 5
num = int(input("Enter a number :"))

if num % 10 == 5:
    print(f"Last digit of enetered {num} is 5")
else:
    print(f"Last digit of enetered {num} is  not 5")