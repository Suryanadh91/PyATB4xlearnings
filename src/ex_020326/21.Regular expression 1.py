# Regular expression (Reg ex) re module - import re module to reg ex
# syntax re.search(pattern,

import re
message = "The current Python version is 3.13 and older version is 3.04, 3.08, 3.10."
print("Python" in message)
# using re module, if match found returns match object, else returns None
match = re.search("Python", message)
print(match)

if re.search("Python", message):
    print("Found")
else:
    print("Not found")
# from re.search using span doing string slicing
slice_str = message[12:18]
print(slice_str)
# using meta char [0-9] below it search for 2 consecutive digits 0 to 9 hence in returns match as 13 from 1st 2 digit decimal in string

match_obj = re.search("[0-9][0-9]", message)
print(match_obj) # op: match 13

# using .(dot) meta char it matches any char except new line char \n
match_obj = re.search("[0-9][.][0-9][0-9]", message)
print(match_obj) # here exactly . matches . only not as meta char

print("#"*50)

match_obj = re.search("[0-9][0-9]", "Roll:352")
print(match_obj) # op: match 35
match_obj = re.search("[0-9][0-9][0-9]", "Roll:352")
print(match_obj) # op: match 352
print("#"*50)

# match_obj is 2026 - 0-9 take 2, . takes 0, 0-9 2, 0-9 6 => 2026
message_1 = "This year is 2026"
match_obj = re.search("[0-9].[0-9][0-9]", message_1)
print(match_obj)

# special char [A-Z][a-z]
# r"" is raw string otherwise in consider /n as new line
str = r"Old/new"
pattern = "[A-Z][a-z][a-z].[a-z]"
# [A-Z] matches => Uppercase letter O, . matches => - /
match_obj = re.search(pattern,str)
print(match_obj)
print("#"*50)

# \d matches any digit char similar to [0-9]
s1 = "Python3.14"
pat = r"[a-z][a-z][a-z]\d"
mobj = re.search(pat, s1)
print(mobj)
# \D consider any char except a digit
pat = r"[a-z][a-z][a-z]\D"
mobj = re.search(pat, s1)
print(mobj)
print("#"*50)

# \s matches white space, tab and \n new line
s2  = "Surya 3.14"
pat_s = r"[a-z][a-z][a-z]\s"
mobj = re.search(pat_s, s2)
print(mobj)
# \S any char except space, tab or new line
pat_S = r"[a-z][a-z][a-z]\S"
mobj = re.search(pat_S, s2)
print(mobj)
print("#"*50)

# \w - matches [A-Z][a-z][0-9]_
S3 = "Python_3@.14"
pat_w = r"[A-Z][a-z][a-z][a-z][a-z][a-z]\w[0-9]"
mobj = re.search(pat_w, S3)
print(mobj)
# \W - matches except [A-Z][a-z][0-9]_
pat_W = r"\W\W"
mobj = re.search(pat_W, S3)
print(mobj)