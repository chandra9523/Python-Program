#Write a python program to find the average of 3 numbers

print("Average of three number")
num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
num3 = int(input("Enter third number = "))

avg = (num1 + num2 + num3)/3

print(f"average of {num1},{num2} and {num3} = {round(avg,2)} ")