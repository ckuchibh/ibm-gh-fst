num = int(input("Enter a number: "))
print()
print(f"Multiplication table of {num} is given below")
print()
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")