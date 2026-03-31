#write a python program to calculate grade based on percentage of marks

percent = int(input("enter a marks percentage :"))

if percent >90:
    print("Grade A")
elif percent > 80:
    print("Grade B")
elif percent > 70:
    print("Grade C")
elif percent > 60:
    print("Grade D")
else:
    print("Grade F")