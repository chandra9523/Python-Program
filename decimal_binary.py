#Write a python program to convert decimal to binary
decimal = int(input("Enter Decimal Number = "))
rev = ''
while decimal > 0:
    r = decimal%2
    rev = str(r) + rev
    decimal = decimal//2
print(rev)

