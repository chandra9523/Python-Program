##write a program to find the type of triangle(equilateral,isosceles,scalene)
side1 = float(input("enter 1st side of triangle :"))
side2 = float(input("enter 2nd side of triangle :"))
side3 = float(input("enter 3rd side of triangle :"))

if side1==side2==side3:
    print(f"Equilateral Triangle have all side equal, side1 ={side1},side2 = {side2}, side3 ={side3}")
elif side1==side2 and side2!=side3 or side1!=side2 and side2==side3 or side1==side3 and side2!=side3:
    print("Triangle is isosecles triangle as out of 3 sides any 2 sides are equal")
else:
    print(f"Triangle is scalene triangle as all the three sides are of different length")