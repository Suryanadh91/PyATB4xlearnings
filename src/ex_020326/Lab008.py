# Tuples are stored in () and elements are fixed

t1 = ("Python",2,3.4,True,None)
print(t1, type(t1))

# type casting
l1 = [1,2,3,4,5]
print(l1, type(l1))
t1 = tuple(t1)
print(l1, type(t1))
fruits = ["apple", "banana", "cherry"]
print(fruits, type(fruits))
fruits = tuple(fruits)
print(fruits, type(fruits))

# indexing, concatenation, repetition, membership,count,min,max,sum
student_detail1 = (352,"Surya")
student_detail2 = (78,78,89,98,87.5)
student_details = student_detail1 + student_detail2 # Concatenation
print(student_details, type(student_details))
print("Surya" in student_detail1) # membership
print("Surya" in student_detail2)
print(98 not in student_detail1)
print(98 not in student_detail2)

t1 = ("class 10",500) # repetition
print(t1 * 3)

print(student_details.count(78))
print(student_details.index("Surya"))
print(student_detail2.index(78)) # it gives the index of 1st occurance
print(f"biggest number:max(student_detail2)")
print(f"smallest number:min(student_detail2)")
percentage = sum(student_detail2)/500*100
print(percentage)
print(f"percentage of student is {percentage}")

# tuples and strings are immutable(can't be modified), list is mutable

# t1 = (1,2,3) gives error
# t1.append(4)
# print(t1)

s1 = "Python is fun"
s1.replace("Python", "Java")
print(s1) # after still there is not as strings are immutable, it can be stored as a new string
s2 = s1.replace("Python", "Java")
print(s2)

l1 = [1,2,3,4,5]
print(id(l1))
print(type(l1))
l1.append(6)
print(id(l1))
print(l1)

f1 = ["mango", "banana", "cherry"]
print(f1)
f1[-1] = "apple" # reassigning of elements (mutability)
print(f1)

# Sets {} are non-sequential collection of elements, indexing and slicing of sets is not allowed
# sets don't allow duplicates in elements
set1 = {10,"python",3.7,True}
print(set1) # the OP doesn't follow sequence
print(type(set1))
print(len(set1))

# slicing, concatenation, repetition is not possible in sets
nums_1 = {1,3,6,-1,2.5}
print(nums_1,id(nums_1))
print(1 in nums_1) # membership operators in not in
print(10 not in nums_1)
nums_1.add(10)  # adding element to set
print(nums_1,id(nums_1))
nums_1.add(3)
print(nums_1,id(nums_1))
nums_1.remove(10) # if element present it removes if not error will be displayed
print(nums_1,id(nums_1))
nums_1.discard(10) # if element present it removes if not no error will be displayed
print(nums_1,id(nums_1))

days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(days, type(days))
days = set(days)
print(days,type(days))
# difference betweens 2 sets
weekends = {"Sat", "Sun"}
print(weekends, type(weekends))
weekdays = days.difference(weekends)
print(weekdays, type(weekdays))


student1 = {"maths","biology","english","physics","chemistry"}
student2 = {"physics","chemistry","english","computers"}
student3 = {"english","hindi","snaskrit"}
common_subjects = student1.intersection(student2,student3) # gives the common from both sets
print(common_subjects)
common_subjects = student1 & student2 & student3# it also acts as intersection
print(common_subjects)
all_subjects = student1.union(student2,student3) # gives all subjects from both students
print(all_subjects)
all_subjects = student1 | student2 | student3
print(all_subjects)

# Frozen sets are immutable
fset1 = frozenset({"Strawberry", "banana", "cherry"})
print(fset1,type(fset1))
fset2 = frozenset({"Apple", "banana", "cherry"})
print(fset2,type(fset2))
print(fset1 & fset2) # common elements from both sets
print(fset1 | fset2) # all elements from both sets
print(fset1 ^ fset2) # differnce elements from both sets
print(fset2 - fset1) # it gives uncommon element from fset2
print(fset1 - fset2) # it gives uncommon element from fset1

