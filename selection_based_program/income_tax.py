#Write a python program to calculate income tax on the basis of income slab

income = float(input("Enter income of an employee:"))

if income < 1200000:
    print("No Tax")
elif income >1200000 and income <1500000:
    tax = 0.05*(income-1200000)
    print(f"tax = {tax}")
elif income >1500000 and income <2000000:
    tax = 0.10*(income-1200000)
    print(f"tax = {tax}")
else:
    tax = 0.30*(income-1200000)
    print(f"tax = {tax}")