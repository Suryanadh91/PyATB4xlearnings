# Print function
name = 'Surya'
age = 20
phn = 9494552084
print(name,age,phn)
# default print function use space separator
print(name,age,phn, sep=" ")
print(name,age,phn, sep=",")
print(name,age,phn, sep="-")
print(name,age,phn, sep="\n")#backward slash n gives new line as separator
print(f"name = {name}\nage = {age}\nphone = {phn}")

# Input function is used to take input from user

name = input("Enter your name: ")
age = int(input("Enter your age: "))
phone = int(input("Enter your phone number: "))
print(f"name = {name}\nage = {age}\nphone = {phone}")

"""
# if enter 3 coluns above n below a program it will be commented
# by default input function takes the input as string
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
sum = num1 + num2
print(sum) # instead of sum string concatenation happens
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
result = num1 + num2
print(result)"

Year = int(input("Enter current year: "))
age = int(input("Enter your age: "))
birth_year = Year - age
print(birth_year)

# Numeric functions

list = 1,2,4,8,67,90,86,-34,-2
print(max(list)) # max number in list
print(min(list)) # min number in list
print(abs(-234)) # absolute number
print(pow(2,4)) # 2 power of 4