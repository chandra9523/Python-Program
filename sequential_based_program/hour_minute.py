#Write a python program to convert minutes into hours and minutes

min = int(input("Enter time in minutes :"))

hour = min//60
minutes = min%60

print(f"In {min} minutes there is {hour}hrs and {minutes}mins")