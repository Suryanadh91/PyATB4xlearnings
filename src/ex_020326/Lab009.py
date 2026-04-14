# Dictionaries are key value pairs in {} {key1:value1, key2:value2}, they are mutable

groceries = {'milk':30, 'biscuit':50, 'rice':1500, "bread":50}
print(groceries)
print(type(groceries))
print(groceries['milk'])
groceries['rice'] = 1600
print(groceries)
groceries['eggs'] = 150 # same format to update or add new item in dict
print(groceries)

marks = {'maths':89, 'physics':92, 'chemistry':80, 'english':75}
print(marks['maths'])
print(marks.get('physics')) # both methods are used to fetch
print(marks.get('science')) # gives none when element not present in dict
# print(marks['biology']) gives error as element not present in dict
print(marks.get('sanskrit',65)) # the element is not present in dict instead of none it gives the default value mentioned as 65
# membership operators works with key only not with value
print('maths' in marks)
print('science' in marks)
print(89 in marks) # gives false as value is  not considered in dict for membership operators
print('sanskrit' not in marks)
print('physics' not in marks)

groceries_1 = {'carrot':40, 'potato':50, 'banana':30, 'mango':20}
groceries_2 = {'rice':1500, 'bread':500, 'milk':50}
# update()
groceries_1.update(groceries_2) # update the dict with elements from other dict
print(groceries_1)
# pop()
groceries_1.pop('milk') # deletes the element
print(groceries_1)
# duplicate keys are not allowed and dict reads from end to start so carrot 60 is considered instead of 40
groceries_3 = {'carrot':40, 'potato':50, 'banana':30, 'mango':20, 'carrot':60}
print(groceries_3)
# not allowed keys = lists,sets,dict - mutable
# allowed keys = int,float,str,bool,tuple - immutable
# values can be ant data types
student_1 = {'id':1, 'name':'Surya', 'marks':[89,90,85.5]} # list inside value of dict
print(student_1['marks'][1])
student_2 = {'id':2, 'name':'Sivansh', 'marks':{'eng':89,'sic':90,'math':85.5}} # dict inside value of dict
print(student_2['marks']['eng'])
# fetch the keys pof dict
print(student_1.keys(), student_1.values())
print(student_1.keys(), student_2.values())
print(student_1.items(),type(student_1.items()))

