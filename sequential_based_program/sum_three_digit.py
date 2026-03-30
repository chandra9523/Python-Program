#Write a python program to find the sum of digit of 3 digit number

num = int(input("Enter 3 digit number:"))
num1 = num
sum = 0

while num1 >0:
    rem = num1%10
    sum = sum + rem
    num1 = num1//10
print(f"Sum of {num} each digit is {sum}")