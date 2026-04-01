#write a program to check whether a charcter is uppercase,lowercase,digit, or special symbol
#Ascii value A to Z(65 to 90)
#a to z(97 to 122)
#0 to 9(48 to 57)

ch = input("Enter character : ")

ascii_ch = ord(ch)

if ascii_ch >=65 and ascii_ch <=90:
    print(f"{ch} is Uppercase")
elif ascii_ch >=97 and ascii_ch <=122:
    print(f"{ch} is lower case letter")
elif ascii_ch >=48 and ascii_ch <=57:
    print(f"{ch} is digit")
else:
    print(f"{ch} is special symbol")
