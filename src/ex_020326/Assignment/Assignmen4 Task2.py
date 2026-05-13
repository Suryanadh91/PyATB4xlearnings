# Task 2
while True:
    try:
        text1 = input("Enter text to write to the file:")
        if text1 != "Hello, Python!":
            raise ValueError("Invalid input! You must enter exactly: Hello, Python!")
        with open("output.txt", "w") as my_file:
            my_file.write("\n" + text1)
        print("Data successfully written to output.txt.\n")
        break
    except ValueError as ve:
        print(f"Input Error: {ve}")

while True:
    try:
        text2 = input("Enter additional text to append:")
        if text2 != "Learning file handling in Python.":
            raise ValueError("Invalid input! You must enter exactly: Learning file handling in Python.")
        with open("output.txt", "a") as my_file:
            my_file.write("\n" + text2)
        print("Data successfully appended.\n")
        break
    except ValueError as ve:
        print(f"Input Error: {ve}")

print("Final content of output.txt:",end=" ")
with open("output.txt", "r") as my_file:
    print(my_file.read())

