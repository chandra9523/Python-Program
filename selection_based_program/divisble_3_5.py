#write a program to check a number is divisble by both 3 and 5

num = int(input("Enter a number :"))

if num%3==0 and num%5==0:
    print(f"{num} is divisble by both 3 and 5")
else:
    print(f"{num} is not divisble by both 3 and 5")

