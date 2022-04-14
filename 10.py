a = input("enter your name: ")
print(f"your name is: {a}")

a = input("enter your age: ")
result = 30 + int(a)
print(f"in 30 years you will be: {result}")

def name_input(a):
    a = input("enter your name: ")
    return a

b = name_input("eran")
print(b)

a = int(input("enter first number"))
b = int(input("enter second number"))
if a < 5:
    print("lower than 5")

if a < 10:
    print("lower than 10")

def check_lower(c, d):
    if c < d:
        print(f"lower than {d}!")

check_lower(a , 5)
check_lower(b, 10)