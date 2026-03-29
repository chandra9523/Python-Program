#write a python program to swap two number

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))

print(f"numbers before swapping is num1 ={num1} and num2 ={num2}")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"numbers after swapping is num1 ={num1} and num2 ={num2}")