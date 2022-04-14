#import fibo
from fibo import fib
from  fibo import fib as my_fib
#fibo.fib(100)
#fib(100)

#my_fib(100)



def square(x):
    #print(x**2)#יותר נכון להגדיר משתנה ואז אותו להחזיר
    result = x * x
    return result

a = square(5)
print(a)

def square_1(d):
    #tupple in the return
    result = d * d
    return result, "blabla"

print(square_1(5))

def my_print(output):
    if output > 5:
        print(output)
    else:
        print("output smaller than 5")

my_print(6)
my_print(4)