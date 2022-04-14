#שגיאות בפייתון

#f40r i in range(100):# שגיאת syntax
#    print(i)
try:
    a = int(input("enter first num: "))
    b = int(input("enter sec num: "))

    result = a / b
    print(result)
except BaseException as e:
    print(f"somethind went wrong: {e.args}")
print("finished")

#בתרגיל זה חלוקה ב -0 מוציאה שגיאה

try:
    a = int(input("enter first num: "))
    b = int(input("enter sec num: "))

    result = a / b
    print(result)
except ZeroDivisionError as e:
    print("COULD NOT DIVIDE BY ZERO")
except ValueError as e:
    print("one of the variables is not a number")
except BaseException as e:
    print("unknown error: " +str(e.args))
#print("finished")