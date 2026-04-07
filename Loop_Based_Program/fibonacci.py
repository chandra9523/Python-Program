#print fibonacci series upto Nterms

num = 20

a=0
b=1
c= a+b
print(a,b,c)
sum = 0
for i in range(2,num+1):
    a = b
    b = c
    c=a+b
    print(c, end =' ')
    sum = sum + c
print("\n")
print("\n")

print(f"sum of {num} fibonacci series number is {sum}")
