# Functions
# user defined functions syntax
# def function_name(arg1, arg2, argn):
#     statement1
#     statement2
#     .
#     .
#     .
#     statementn
def greeting(name):
    print(f"Hi {name} Good morning!")
    print("It is a beautiful day!")
# Calling function
greeting('Surya')
greeting('sivansh')

def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
def add(num1, num2):
    result = num1 + num2
    print(f"Result: {result}")

even_or_odd(5)
add(1, 2)

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("#############################################")
# mutiple arg and statements with multiple returns
def arithmetic(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    return addition, subtraction, multiplication
val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))
res1, res2, res3 = arithmetic(val1, val2)
print(f"Addition of {val1} and {val2}: {res1}")
print(f"Subtraction of {val1} and {val2}: {res2}")
print(f"Multiplication of {val1} and {val2}: {res3}")
print("#############################################")
# positional arguments 3 refer to a 4 refer to b based on the position
def summ(a, b):
    return a + b
result  = summ(3,4)
print(result)
print("#############################################")
# default arguments, default arguments should not be placed before positional arguments
def summation(a, b=5):
    return a + b
result = summation(3)
print(result) # a = 3, by default b = 5
result = summation(3,4)
print(result) # a = 3 and default value is replaced by  4
print("#############################################")
# keyword arguments,
def addition(a, b=2, c=4):
    print(f'a={a}, b={b}, c={c}')
    return a + b + c
result = addition(2, 3)
print(result)
result = addition(c=3, b=6, a=9) #arguments are assigned by the name irrespective of position or default values
print(result)
print("#############################################")
# *args variable length positional args,
# eg: def pizza(*toppings, base)  only 1 *args can be part of a function
# def pizza(base, *toppings)  *args can't placed after a argument
# def pizza(*base, *toppings) not possible
def sum_of(*args):
    print(type(args)) # to check the type of args
    print(args)# to check the args
    return sum(args) # used builtin function sum
result = sum_of(1,2,3,4,5,6)
print(result)
print("#############################################")

def student_details(id, name, *marks):
    # doc_string written below show what the function does
    """this function calculate percentage of the students
    it consists of
    student id
    student name
    student marks"""
    if len(marks) == 0:
        print("Student with ID", id, name,"is absent") # this condition is written to bypass the error as no marks present
    else:
        percentage = sum(marks)/ len(marks)
        print(f"Student with ID {id} {name} secured {percentage}%")
help(student_details) # display doc_string in the function
student_details(352, 'Surya', 89.0,78.0,90.5,88.5,78.5,98.7)
student_details(621, 'Sivansh', 98,87,88,92,91,96,)
student_details(220,"Revathi")
