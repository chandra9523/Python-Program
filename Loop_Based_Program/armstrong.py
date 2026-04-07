#Check whether a number is an armstrong number

num = input("enter number :")
num1 = num
sum = 0
for n in num:
    sum = sum + int(n)**3
print(sum)
if int(num1) == sum:
    print("armstrong")
else:
    print("not armstrong")