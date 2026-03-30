#write a program to print all digit of 3 digit number

num = (input("Enter 3 digit number:"))

while num > 0:
    rem = num%10
    num = num//10
    print(rem)
