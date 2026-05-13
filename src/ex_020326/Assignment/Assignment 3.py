def factorial(n):
    fact = 1
    while n > 1:
        fact = fact * n
        n -= 1
    return fact

# factorial with recursion
def fact_recursive(n):
    if n == 1:
        return 1
    else:
        factorial = n * fact_recursive(n-1)
        return factorial

num = int(input("Enter a number: "))
fact1 = factorial(num)
print(f" Factorial of {num} is: {fact1}")
fact2 = fact_recursive(num)
print(f" Factorial of {num} is: {fact2}")
print("===============================")
import math
number = int(input("Enter a number: "))
sqrt = math.sqrt(number)
print(f" Square root : {sqrt}")
logarithm = math.log(number)
print(f" Logarithm : {logarithm}")
sine = math.sin(number)
print(f" Sine: {sine}")
