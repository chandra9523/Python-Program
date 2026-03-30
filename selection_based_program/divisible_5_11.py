#write a python program to check whether number is divisble by 5 and 11

num = int(input("Enter a number :"))

if (num % 5 ==0 and num % 11 == 0):
    print(f"{num} is divisble by 5 and 11")
else:
    print(f"{num} is not divisble by 5 and 11")