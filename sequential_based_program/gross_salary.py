#Write a python program to calculate gross salary(basic + HRA +DA)
basic = float(input("Enter basic salary ="))
hra = float(input("Enter HRA:"))
da = float(input("Enter DA:"))

gross_salary = basic + hra + da
print(f"gross salary :{gross_salary}")