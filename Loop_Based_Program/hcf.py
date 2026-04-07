#find hcf of two number
num1 = int(input("enter first number:"))
num2 = int(input("enter second number"))

first_num = num1
sec_num = num2
r = 1
while (r>0):
    #q=num1//num2
    r = num1%num2
    num1=num2
    num2 = r
    
if r == 0:
    print(f"HCF OF {first_num} and {sec_num} = {num1}")

