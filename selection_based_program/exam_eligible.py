#write a python program to check eligibility for exam(attendance >= 75%)

atdnce = int(input("Enter attendance:"))

if atdnce >= 75:
    print(f"Eligible to give exam as attendance is {atdnce}%")
else:
    print(f"Not eligible to give exam as attendance is below 75% i.e. {atdnce}%")