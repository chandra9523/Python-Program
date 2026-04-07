#find factorial of number
num = int(input("Enter the number whose factorial you want :"))
num1=num
fact = 1
while(num >0):
    fact=fact*num
    num-=1

print(f"Factorial of {num1} is {fact}")