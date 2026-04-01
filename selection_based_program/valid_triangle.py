#write a program to check whether three sides from a valid triangle
side1 = int(input("enter 1st side of triangle :"))
side2 = int(input("enter 2nd side of triangle :"))
side3 = int(input("enter 3rd side of triangle :"))

if side1 + side2 > side3 and side2+side3>side1 and side1+side3 >side2:
    print("Valid Triangle")
else:
    print("not valid triangle")