#Write a python program to check BMI Category(underweight, normal, overweight)

bmi = float(input("Enter your bmi:"))

if bmi < 18.5:
    print("You are underweight")
elif bmi >18.5 and bmi <24.9:
    print("Your weight is normal") 
else:
    print(" You are overweight. Take care")
