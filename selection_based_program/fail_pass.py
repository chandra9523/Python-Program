#write a python program to check student failed or passed(pass>=40)

marks = int(input('Enter Marks:'))

if marks >= 40:
    print(f"Student passed as he scored {marks} marks")
else:
    print(f"Student failed as he scored {marks} marks")