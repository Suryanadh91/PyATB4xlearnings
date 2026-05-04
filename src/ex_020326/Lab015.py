# A function calls itself until a condition is not met is called recursive function
# It has 2 parts 1. Base/Terminal condition, 2.Recursive condition
# factorial without recursion
def fact(n):
    factorial = 1
    while n > 1:
        factorial = factorial * n
        n -= 1
    return factorial
print(fact(4))
print("###############################")
# factorial with recursion
def fact_recursive(n):
    if n == 1:
        return 1
    else:
        factorial = n * fact_recursive(n-1)
        return factorial
print(fact_recursive(4)) # function is called until n =1 and it calculates in reverse 1*2*3*4
print("###############################")
n = 4 # Global variable
def fn():
    n = 5 # local variable
    print("Local", n)
fn()
print("Global", n)
print("###############################")
n = 1
def fun():
    global n # we are using local variable as global variable
    n = 5
    print("Local", n)
fun()
print("Global", n)
print("###############################")
# passing a function as arg in another function
def add1(n):
    return n + 1

def sqaure(n):
    return n ** 2

result = sqaure(add1(3)) # fun add1 is passed as arg in fun square
print(result)
print("###############################")
# Lambda function is function with out name
# syntax lambda argument: expression

fun = lambda a: a + 1
print(fun(5))

res = lambda a,b: a + b
print(res(2,3))
print("###############################")
# filter
seq = [1,2,3,4]
filtered_output = filter(lambda x: True if x%2 != 0 else False ,seq)
print(filtered_output) # we need to specify the type as list to see the objects in filter
print(f"The ood numbers are {list(filtered_output)}")
print("###############################")
# Map
mapped_output = map(lambda x: True if x%2 != 0 else False ,seq)
print(mapped_output) # we need to specify the type as list to see the objects in filter
print(f"The ood numbers are {list(mapped_output)}") # map doesn't filter the objects, it captures all the iterations of the objects
print("###############################")
map_output = map(lambda x: x**2, seq)
print(map_output)
print(f"The square of the seq elements are {list(map_output)}")
print("###############################")
# module in python is a file with .py
# there are modules like builtin modules(math, random, etc) and user defined modules
# Syntax to import modules
# import module name eg: import math
import math
sq_rt = math.sqrt(100)
print(sq_rt)
radius = 5
area = math.pi * (radius ** 2)
print(area)
# syntax to import few functions/variables from module
# import function eg: from random import randint
from random import randint
dice = randint(1,6)
print(dice)
# syntax give alias name to a module imported
# import module name as alias name
import datetime as dt
time = dt.time(hour=8,minute=0,second=59)
print(time)
# userdefine modules created a file with name Arthimatic
# ** when import a module and if there is any executable code it will be executed along with the imported function
import Arithmetic

a = 100
b =50

sq_root = Arithmetic.sqaureroot(a)
print(sq_root)

print(f"Addition {Arithmetic.addition(a, b)}, subtraction {Arithmetic.subtraction(a, b)},multiplication {Arithmetic.multiplication(a, b)}")

