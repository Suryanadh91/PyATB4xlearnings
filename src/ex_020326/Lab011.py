# for loop same syntax for list,tuple,strings
l = ['mike',23,2002]
for i in l:
    print(i)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
for x in ['surya',35,1991]:
    print(x)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
s = 'Surya'
for x in s:
    print(x)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
for i in range(1,11): # 1 to 10
    print(i)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
for i in range(1,11,2): # skip 1 digit
    print(i)
# Conditional or relational statements
# syntax of if
# if condition:
age = int(input('what is your age?'))
if age >= 18:
    print('you are an adult, you can vote!')
print('age check done')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
# if else
# if condition:
#    code executes when it is true
# else:
#    code executes when it is false
if age >= 18:
    print("you can vote")
else:
    print("you can not vote")
print("age check done")
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
num = int(input('what is your number?'))
if num % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
num = int(input('what is your number?'))
if num >= 0:
    print('The number is positive')
else:
    print('The number is negative')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
marks = int(input('what is your marks?'))
if marks >= 90:
    print('A grade')
elif marks >= 80 and marks < 90:
    print('B grade')
elif 70 <= marks < 80:# standard way of comparison
    print('C grade')
elif marks >= 50 and marks < 70:
    print('D grade')
else:
    print('F grade')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
marks = int(input('Enter your marks?'))
if marks >= 40:
    print('Congratulations! you passed the exam')
    if marks >= 90:
        print('A grade')
    elif marks >= 80 and marks < 90:
        print('B grade')
    elif 70 <= marks < 80:  # standard way of comparison
        print('C grade')
    elif marks >= 50 and marks < 70:
        print('D grade')
    else:
        print('F grade')
else:
    print('You failed the exam')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
# ternery operator means a single line code
# true expression if cond false expression else cond
num = int(input('what is your number?'))
print("number is even") if num % 2 == 0 else print("number is odd")

