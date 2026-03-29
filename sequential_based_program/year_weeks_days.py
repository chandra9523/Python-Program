#write a python program to days into years, weeks and days

day = int(input("enter the number of days ="))

year = day//365
remaing_days = day%365
week = remaing_days//7
remaining_days = remaing_days % 7



print(f"In {day} days there is {year} years,{week}weeks and {remaining_days}days")


