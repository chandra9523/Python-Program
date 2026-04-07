#Print the multiplication table of a number

num = int(input("Enter number whose multiplication you want to find :"))

for i in range(1,11):
    print(f"{num} * {i} = {num*i}")