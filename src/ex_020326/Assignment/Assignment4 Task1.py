"""Task 1"""

# Part 1
with open("sample.txt","xt") as my_file:
    my_file.write("This a sample text file.\n")
    my_file.write("It contains multiple lines.\n")
# Part 2 => to check for exception run only part in separate file
try:
    with open("sample.txt","rt") as my_file:
        lines = my_file.readlines()
        line_num = 1
        for line in lines:
            print(f"Line {line_num}: {line.rstrip("\n")}")
            line_num += 1
except FileNotFoundError:
        print("Error: The File 'sample.txt' was not found.")
except FileExistsError:
    print("Error: The file exists!")


