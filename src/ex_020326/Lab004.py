# Area of triangle
side_a = float(input('Side a: '))
side_b = float(input('Side b: '))
side_c = float(input('Side c: '))
s = side_a + side_b + side_c/2
print(s)
area_of_triangle = (s*(s-side_a)*(s-side_b)*(s-side_c)) ** 0.5 # ** 0.5 it gives sq root of number
print(round(area_of_triangle, 2))

#area of right angle triangle 1/2*b*h
b = float(input("breadth_of_triangle "))
h = float(input("height "))
area = (b*h)/2
print("Area of the triangle: ", area)

# Simple interest P*R*T/100 p = principal amt, R = rate of intrst, T = Duration

principal = float(input('enter principal amount: '))
rate = float(input('enter interest rate: '))
time = float(input('enter time: '))
SI = (principal * rate * time)/100
print("simple interest is:", SI)

# Compound interest Amount - primcipal, amount = p(1+r/100)pwr t
principal = float(input('enter principal amount: '))
rate = float(input('enter interest rate: '))
time = float(input('enter time: '))
amount = principal * pow((1+rate/100),time)
#amount = principal * (1+rate/100) ** time # another way to get amount
print(round(amount,2))
CI = round(amount - principal,2)
print("Compound interest is:",CI)