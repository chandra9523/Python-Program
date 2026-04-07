# print 1 3 5 7... N

n = int(input("Enter last number  upto which odd number is required : "))

for i in range(1, n+1):
    if i % 2!=0:
        print(i, end =' ')
        