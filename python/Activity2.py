num = int(input("Enter a number: "))

if num != 0:
    if num %2==0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
else:
    print("0 is neither Even nor Odd")

