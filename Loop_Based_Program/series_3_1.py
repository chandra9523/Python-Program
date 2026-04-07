#Print Series : 2,6,7,21,22,66(pattern multiply by 3, then +1)

num = int(input("Enter number upto which you want the series:"))
print(2)
for i in range(2, num+1):
    num1 = i*3
    print(num1)
    if num1 % i == 0:
        print(num1+1)