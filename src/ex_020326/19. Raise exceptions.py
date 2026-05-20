# Raising exceptions
# syntax raise exception name

salary = float(input("Enter your salary: "))
if salary < 0:
    raise ValueError("Your salary cannot be less than or equal to 0")
else:
    print(f"Your salary is {salary}")

age = float(input("Enter your age: "))
if age < 0:
    raise Exception("Your age cannot be less than or equal to 0")
elif age >= 18:
    print("you can vote")
else:
    print("you can not vote")
print("#################################")
json module
import json

students = {'student1':{'roll':'101','name':'surya','percentage':98.5,'sports': True},
            'student2':{'roll':'103','name':'Sivansh','percentage':91.5,'sports': False},
            'student3':{'roll':'105','name':'Hari','percentage':90.5,'sports': True}}
print(students)
print(type(students))
# dump is used to write data in json
with open("students.json", "w") as json_file:
    # indent=4 is used to enter data in json format
    json.dump(students, json_file, indent=4)
print("#################################")

# load is used to read json
with open("students.json", "r") as json_file:
    students = json.load(json_file)

print(students)
print(type(students))

# update()
# read old data from json file
with open("students.json", "r") as json_file:
    data = json.load(json_file)
# update function used and data of students dict is modified with new data above
data.update(students)

# dump - write updated data in json
with open("students.json", "w") as json_file:
    json.dump(students, json_file, indent=4)
with open("students.json", "r") as json_file:
    students = json.load(json_file)
    print(students)
    print(type(students))

# Update operation when file not found
'''
try:
    with open("students.json", "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    with open("students.json", "w") as json_file:
        json.dump(students, json_file, indent=4)
else:
    # update operation
    data.update(students)
    # dump operation
    with open("students.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
    with open("students.json", "r") as json_file:
            students = json.load(json_file)
            print(students)
'''