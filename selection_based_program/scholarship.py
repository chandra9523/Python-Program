#write a python program to check if student gets a scholarship(marks + income condition)

marks = int(input("Enter Marks:"))
income_condition = input("Enter income condition:")

if marks >90 and income_condition == 'poor':
    print(f"Eligible for scholarship as {marks}marks is above 90% and income_condition is {income_condition}")
else:
    print(f"Not Eligible for scholarship as {marks}marks is below 90% and income_condition is {income_condition}")