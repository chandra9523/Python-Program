#Check whether number is pallindrome

num = int(input("enter number :"))

num1 = num
rev = 0
r= 0

while num >0:
    r = num % 10
    rev = rev*10 + r
    num = num//10


if rev == int(num1):
    print(f"{num1} is pallindrome")
else:
    print(f"{num1} is not pallindrome")