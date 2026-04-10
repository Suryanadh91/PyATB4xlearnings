#Type casting of Boolean
val1 = True
print(type(val1))
print(val1)

val2 = 'Surya'
print(type(val2))
print(val2)
val3 = bool(val2)
print(type(val3))
print(val3)
# empty string will give false
# space is considered as not empty it will be true
# None is considered as flase in bool
val11 = None
print(type(val11))
val12 = bool(val11)
print(type(val12))
print(val12)#false

val21 = ''
print(type(val21))
print(val21)
val22 = bool(val21)
print(type(val22))
print(val22)#false

val4 = 13.21
print(type(val4))
print(val4)
val5 = True
print(type(val5))
print(val5)

val6 = 0
print(type(val6))
print(val6)
val7 = bool(val6)
print(type(val7))
print(val7)

val8 = -13
print(type(val8))
print(val8)
val9 = bool(val8)
print(type(val9))
print(val9)

val10 = int(True)
print(type(val10))
print(val10) #true will give values as 1

val13 = float(False)
print(type(val13))
print(val13)# flase will give value as 0

#Arthimater operators
n1 = 10
n2 = 5
n3 = 3
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2) #it gives in float value
print(n1 // n2) # floor division operator give op in integer
print(n1 // n3)
print(n1 % n2) # modulus operator give reminder as op
print(n3 ** 2) # exponent operator give power of value 2 power 3 = 8

# Assignment operators
x = 10 # = assignment operator
y = x + 10
print(x)
print(y)

z = 10
print(z)
z += 1 # z = z + 1 += is compound assignment operator
print(z)
z -= 6
print(z)
z *= 5
print(z)
z /= 5
print(z)

# Comparison operators ==,!=,>,<,>=,<=
num1 = 100
num2 = 90
num3 = 90

print(num1 == num2)
print(num2 == num3)
print(num1 != num2)
print(num2 != num3)
print(num1 > num2)
print(num2 < num1)
print(num1 >= num2)
print(num2 >= num3)
print(num1 <= num2)
print(num2 <= num3)
print('#######################')
#logical operators and,or,not

con1 = True
con2 = False
con3 = True
con4 = False
print(con1 and con2)
print(con2 and con3)
print(con1 and con3)
print(con2 and con4)
print('###########################')
print(con1 or con2)
print(con2 or con3)
print(con1 or con3)
print(con2 or con4)
print('###########################')
print(not con1)
print(not con2)