#write a python program to check division 1st, 2nd, 3rd, Fail

marks = float(input("Enter Marks:"))

if marks > 60:
    print("1st Division")
elif marks > 50:
    print("2nd Division")
elif marks > 40:
    print("3rd Division")
else:
    print("fail")