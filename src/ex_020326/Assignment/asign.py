try:
    # 1. Take user input and validate for text1
    text1 = input("Enter text to write to the file: \n")

    if text1 != "Hello, Python!":
        raise ValueError("Invalid input! You must enter exactly: Hello, Python!")

    with open("output.txt", "w") as my_file:
        my_file.write("\n" + text1)
    print("Data successfully written to output.txt.\n")

    # 2. Take user input and validate for text2
    text2 = input("Enter additional text to append: \n")

    if text2 != "Learning file handling in Python.":
        raise ValueError("Invalid input! You must enter exactly: Learning file handling in Python.")

    with open("output.txt", "a") as my_file:
        my_file.write("\n" + text2)
    print("Data successfully appended.\n")

    # 3. Read and display the final content
    print("Final content of output.txt: ", end="")
    with open("output.txt", "r") as my_file:
        print(my_file.read())
