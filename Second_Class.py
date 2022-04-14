#A
x = 2
y  = 5
if x > y:
    print("BIG")
else:
    print("small")

#B
i = 0
for i in range(0,5):
    i += 1
    print(i)

#C
season = int(input("enter number between 1 -4 to choose season: "))
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")

'''
D.
1. how many times will the following loop run?
2. what will be printed last?
מה זו שאלה D לא הבנתי לאיזו לולאה מתכוונים
'''
#E.
my_age = 45
First_Letter = "E"
Shekel_Dollar = 3.2
Flew_Abroad = False
Apart_No = 126
Add = my_age + Shekel_Dollar

print(my_age, First_Letter, Shekel_Dollar, Flew_Abroad, Apart_No)
print(Add)

#F.

Phone_no = input("Enter your phone number: ")
print("phone number: " , Phone_no)


#G.
def printHello():
    print("hello")
printHello()
def calculate(a, b):
    print(a + b)
calculate(5, 3.2)

#H

def enter_name(name):
    print(name)

enter_name("Eran")

def divide_no(num):
    print(num/2)

divide_no(6)

#I.

def add_two(a, b):
    return a + b

print(add_two(2, 5))
def two_strings(a, b):
    return a + " " + b

print("Eran", "Bar")



#K.
#Create a nested for loop (loop inside another loop) to create
#a pyramid shape:

for i in range (0, 7):
    for j in range(0, 7-i):
        print(" ",end = "")
    for l in range (0, 2*i +1):
        print("0", end = "")
    print("")


#L.

for x in range(7):
    for k in range(7):
        if x == k or x+k == 7-1:
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()

'''
M.
Write a program with the following:
1. Method that gets a number from the user (using input).
2. Method that receive the number from the first method, and
computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)
'''

n = int(input("enter double-digit number: "))

sum = 0

while(n>9):
    digit = n%10
    n= n//10
    sum = n + digit
    print("The total sum of digits is:", sum)



