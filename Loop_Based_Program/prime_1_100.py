for n in range (1,101):
    if n < 2:
        continue
        
    else:
        for num in range(2, (n//2)+1):
            if n % num == 0:
                break
        else:
            print(n)