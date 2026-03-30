#Write a python program to calculate electricity bill(rate*unit)
unit = int(input("Enter the unit consumed:"))
rate = float(input("Enter the rate of electricity:"))

e_bill = unit * rate

print(f"Electricity bil for {unit} unit at {rate}/unit : {e_bill}")