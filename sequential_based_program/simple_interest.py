#write a python program to find the simple interest
print("******Simple Interest Calculation*********")
principle = float(input("enter principle amount = "))
rate = float(input("enter rate of interest = "))
time = float(input("Enter time = "))

simple_interest = (principle*rate*time)/100

print(f"Simple interest for amount Rs.{principle}/- with rate of interest {rate}% for time {time} years = {simple_interest}")