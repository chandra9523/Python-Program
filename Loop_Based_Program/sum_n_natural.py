#find the sun of first N natural numbers
n = int(input("enter how many natural number sum you want:"))

sum = 0
for i in range(0,n+1):
    sum +=i

print(f"sum of first {n} natural number is {sum}")