# Task 1:

student_list = {"surya": 95, "sivansh":92, "vishwam": 89, "jayadev":93, "jayesh":88}

while True:
    student_name = input("student's name: ").lower()
    try:
        marks = student_list[student_name]
        print(f"{student_name}'s marks: {marks}")
        break
    except KeyError:
        print("name not found")
    except NameError:
        print("name not found")
print("##################################################")
# Task 2:

num_list = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {num_list}")
list1 = num_list[0:5]
print(f"Extracted 1st 5 element: {list1}")
list2 = list(reversed(list1))
print(f"Reversed extracted elements: {list2}")

