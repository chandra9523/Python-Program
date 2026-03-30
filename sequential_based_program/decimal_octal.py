#write a python program to convert decimal to octal

decimal = int(input("Enter a decimal number:"))
oct = ''

while decimal > 0:
    r = decimal%8
    oct = str(r) + oct
    decimal = decimal//8
print(oct)