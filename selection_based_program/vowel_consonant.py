ch = input("enter charcter:")

if ord(ch)>=65 and ord(ch<=90) or ord(ch)>=97 and ord(ch)<=122:
    if ch in 'aeiouAEIOU':
        print(f"{ch} is vowel")
    else:
        print(f"{ch} is consonant")
else:
    print("character not valid")