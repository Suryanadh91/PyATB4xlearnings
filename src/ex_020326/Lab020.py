# Pickle module
students = {'student1':{'roll':'101','name':'surya','percentage':88.5,'sports': True},
            'student2':{'roll':'103','name':'Sivansh','percentage':91.5,'sports': False},
            'student3':{'roll':'105','name':'Hari','percentage':90.5,'sports': True}}
print(students)
print(type(students))
print("#################################")
'''
with open("students_data.txt", "x") as fh:
    # as students is a dict we can't write s txt, so convert dict to str
    fh.write(str(students))
'''
'''
with open("students_data.txt", "r") as fh:
    content = fh.read()
print(content)
print(type(content))
out = dict(content)
# A string cannot be covert to a dictionary
print(out)
'''
# using pickle module
import pickle

# Serialization, file.bin pickle module works with binary files
with open("students_data.bin", "wb") as fh:
    for student in students:
        pickle.dump(students[student], fh)

# Deserialization means reading back the data in pickle binary file
with open("students_data.bin", "rb") as fh:
# as we know the data has 3 records, if we try to fetch data for 4th record which is not present we get EOF error (end of file error)
# """
#     data1 = pickle.load(fh)
#     print(data1,type(data1))
#     data2 = pickle.load(fh)
#     print(data2,type(data2))
#     data3 = pickle.load(fh)
#     print(data3,type(data3))
# """

# if we don't know hom many records are there
    while True:
        try:
            data = pickle.load(fh)
            print(data, type(data))
        except EOFError:
            print("End of file Done!")
            break
print("#################################")
# print records of students with percentage 90+
with open("students_data.bin", "rb") as fh:
    while True:
        try:
            data = pickle.load(fh)
            if data["percentage"] >= 90:
                print(data['name'])
        except EOFError:
            print("Done!")
            break
print("#################################")
# print students record as  a list with percentage 90+
stundets_list_90 = []
with open("students_data.bin", "rb") as fh:
    while True:
        try:
            data = pickle.load(fh)
            if data["percentage"] >= 90:
                stundets_list_90.append(data['name'])
        except EOFError:
            print("Done!")
            break
print(f"students who secured percentage 90 or more are: {stundets_list_90}")