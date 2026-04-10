# String slicing
s1 = "Hello World"
print(s1)
print(len(s1))
print(s1.upper())# converting to upper case
print(s1.lower())# converting to lower case
print(s1[0])# positve indexing it gives 1st char in string
print(s1[-1])# negative indexing gives last char in string
print(s1[1:7:1]) # it starts with index1 and eds with 7-1= 6th index with step1
print(s1[0:11:2]) # when step is given 2 it skips 1 char in printing from index give 0 to 11
print(s1[0:11:3]) # it skips 2 chard as step is 3
print(s1[0:20:2]) # as the last index is exceeding the len by default it stops at last index only
s2 = s1[6:11]
print(type(s2))
print(s2)

# F string basically formatting strings
name = "Surya"
age = 35
subject = "Python"
print(name,"is",age,"years old and he is learning",subject)
print(f"{name} is {age} years old and he is learing {subject}")

sub1 = 80
sub2 = 90
sub3 = 75
percentage = ((sub1 + sub2 + sub3)/300)*100
print(percentage)
print(f"{name} scored {round(percentage,2)} in exams")

# escape sequences
