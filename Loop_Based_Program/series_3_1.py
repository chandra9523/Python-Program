#Print Series : 2,6,7,21,22,66(pattern multiply by 3, then +1)

num = int(input("Enter number upto which you want the series:"))

a= 2
b = a*3
c= b+1
print(a,end = ' ')
print(b, end = ' ')
print(c, end = ' ')

for i in range(2, num+1):
    a = c
    b = a *3
    print(b,end = ' ')
    c = b+1
    print(c,end = ' ')