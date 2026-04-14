# Lists are stored in [] and can be modified
student = ["Surya",35,80] #list
print(len(student))
print(student[0])
print(student[-1])
print(student[0:3])
day_of_week = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
print(f"Last day of week is {day_of_week[-1]}")

# slicing of lists
l1 = [1,2,3,4,5,6,7,8,9,0]
print(l1)
l2 = l1[0:10:2]
print(l2)

# Concatenation of lists
l1 = ["surya",35,9494]
l2 = ["study","Python"]
print(l1+l2)

# Repetition *
print(l2 * 3)

# append() - adds a single item in the end of list
Fruits = ["apple","banana","mango"]
print(Fruits)
print(Fruits.append("apple")) # gives none due to mutability but pear is added
Fruits.append("orange")
print(Fruits)
Fruits.append(["apple","banana","mango"]) # adds as single element as nested list
print(Fruits)
Fruits.remove(["apple","banana","mango"])
print(Fruits)
# insert adds an element at specified place, list.insert(index,element)
Fruits.insert(2,"grapes")
print(Fruits)

# extend() functions adds multiple elements or arguments
Fruits.extend(["papaya","guava"])
print(Fruits)

# remove
Fruits.remove("guava")
print(Fruits)
Fruits.remove("apple") # removes 1st occurring element
print(Fruits)

# Pop removes elements as per index
Fruits.pop(3)
print(Fruits)
Fruits.pop(-1)
print(Fruits)
Fruits.pop() # by default last element will be removed
print(Fruits)

# reverse,sort,count, membership
day_of_week.reverse() # reverse the list
print(day_of_week)

l1 = [2,5,7,9,3,7.4,8,1,4,6,]
print(l1)
l1.sort() # sorts the list by default ascending
print("Sorted list in ascending:",l1)
l1.sort(reverse=True)
print("Sorted list in descending:",l1)
l2 = [1,3,4,5,6,7,8,9,4,3,5,]
print(l2.count(3))
print(f"the list is:{l2}")
num_to_count = int(input("num to count: "))
print(f"{num_to_count} appeared {l2.count(num_to_count)} times")
print(3 in l2) # membership operators
print(0 in l2)
print(10 not in l2)

# Numeric operations
l3 = [1,4,2.1,0.7,5,6,8,9,10] # if the list has strings comparison is not possible
print(f"smallest number is {min(l3)}") # smallest number
print(f"largest number is {max(l3)}") # largest number
print(f"sum of the list is {sum(l3)}") # Sum of

# Nested list

list_1 = [8, 1.8, "Python", True, None, [1, 2, 3, 4, ], 10]
print(len(list_1))
print(list_1[5])
print(list_1[-2][0]) # gets 1 from nested list
list_2 = [[1,3],[2,4],[5,6],[7,8,[9,0]]]
print(len(list_2))
print(list_2[-1][2][-1]) # prints 0 from nested lists
