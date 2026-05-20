# Error handling by try and except
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)

except ZeroDivisionError:
    print("Error: Please enter a number greater than zero.")
except ValueError:
    print("Error: Please enter a numeric value.")
except IndexError:
    print("Error: Please enter a numeric value.")
print("########################################")
try:
    with open("my_file.txt", "rt") as my_file: # with is used to automatically close the file
        data = my_file.read()
except FileNotFoundError as file_not_found:
    print("Error: File not found.")
    print(file_not_found)
else:
    print(data)
print("########################################")
import io
try :
    fh = open("file5.txt", "wt")
    fh.write("Hello World")
except FileNotFoundError as file_not_found:
    print("Error: File not found.")
    print(file_not_found)
except io.UnsupportedOperation as unsupported_operation:
    print("Error: Unsupported operation.")
    print(unsupported_operation)
else:
    fh = open("file5.txt", "rt")
    print(fh.read())
    print("else block")
finally:
    print("Final block")
    fh.close()
