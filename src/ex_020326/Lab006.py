# operations on strings
# + concatination, * repetetion

s1  = "Python"
s2 = "3.08.12"
print(s1 + s2)
print(s1 * 3)

# membership operator in, not in
s1 = "Python is fun"
print("Python" in s1)
print("Z" in s1)
print("Java" not in s1)
print("Python" not in s1)

# comparision of strings
print("Python " == "Python")
print("Python" == "Python")

# Removing space from string using strip
s1 = "   Python    "
print(s1 == "Python") # due to space it is false
print(s1.strip() == "Python") # space is removed and statement is true

# replace
s1 = "we are learning Python"
print(s1)
s2 = s1.replace("Python", "Java")
print(s2)
print(s1.replace('e','E')) #all e are replaced
print(s1.replace('e','E',1)) #onlt 1st e is replaced

# count function, upper(), lower(), title(), captalize()
print(s1.count('e'))
print(f"occurence of 'e' is {s1.count('e')}")
print(f"occurence of ' ' is {s1.count(' ')}") # count of spaces
print(s1.upper())
print(s1.lower())
print(s1.title()) # all initial characters of words are changed to upper case
print(s1.capitalize()) # 1st character is upper case all other will be lower case

# starting and ending of string
print(s1.startswith('w'))
print(s1.endswith('n'))
print(s1.startswith('We')) #false as W is in upper case
print(s1.endswith('Pytho'))