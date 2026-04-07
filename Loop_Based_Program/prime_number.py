#Check whether a number is prime
num = int(input("enter number to check its prime or not:"))
if num ==2:
    print(f"{num} is prime number")
else:
    for n in range (2, (num//2)+1):
        if num % n == 0:
            print(f"{num} is not prime number")
            break
    else:
        print(f"{num} is prime number")