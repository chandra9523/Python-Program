#write a python program to calculate electricity bill using slab rates

unit = int(input("enter a unit of electricity bill consumed:"))
rate = 7.8

if unit > 100:
    ebill = unit*rate
elif unit >70 and unit > 100:
    