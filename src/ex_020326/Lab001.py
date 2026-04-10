# this is comment - which doesn't run.
####4/4/26
print("Hello World")

a = "Hello"
b= "World"
c = a+b
print(c)

s1 = "Helloworld"
s2 = 'we are learning python'
s3 = """hi everyone.
we are looking at srtrings.
bye
"""
s4 = "python"
print(len(s4))
# finding index
print(s4[0])
print(s4[1])
print(s4[2])
print(s4[3])
print(s4[-1]) #last index of s4
#print(s4[7]) # index error no char available

s5 = s1 + s2
s6 = s1 + ' ' + s2 # given space
print(s5)
print(s6)

n1 = 100
print(type(n1))
print(n1)
print(float(n1))
n2 = float(n1)
print(type(n2))
print(n2)
n1 = float(n1) # coverting int data type to float
print(type(n1))
print(n1)

#coverting float to int
num1 = 30.25
print(type(num1))
print(num1)
num1 = int(num1)
print(type(num1))
print(num1)

num2 = 30.95 # it is not rounded to 31 after conversion
print(type(num2))
print(num2)
num2 = int(num2)
print(type(num2))
print(num2)

#int to string
num4 = 1000
print(type(num4))
print(num4)
x = str(num4)
print(type(x))
print(x)

# string charc can't be convert to int or float
#string with numver and charc mixed also can't be convert to int or float
# string with number can be convert to int or float
# type conversion add str and float
lang = 'Python'
version = 3.14
print(lang)
print(type(lang))
print(version)
print(type(version))
#print(lang+version)
version = str(version)
print(type(version))
print(version)
print(lang+version)
print(type(lang+version))