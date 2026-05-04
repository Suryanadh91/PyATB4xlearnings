def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return  num1 - num2

def multiplication(num1, num2):
    return  num1 * num2

def sqaureroot(num1):
    return num1 ** 0.5
print(__name__) # gives __name__ = arithmetic when lab015 runs importing Arithmetic, when arithmetic is executed __name__ = __main__
if __name__ == "__main__": # if with __name__ prevents the execution of below code when the module is imported
    a = 10
    b = 20
    sum = addition(a, b)
    print(sum)

