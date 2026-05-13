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

match_obj = re.search("[0-9][0-9]", "Roll:352")
print(match_obj) # op: match 35
match_obj = re.search("[0-9][0-9][0-9]", "Roll:352")
print(match_obj) # op: match 352
match_obj = re.search("[0-9][.][0-9][0-9]", message)
print(match_obj) # here exactly . matches . only not as meta char
# using .(dot) meta char it matches any char except new line char \n
# match_obj is 2026 - 0-9 take 2, . takes 0, 0-9 2, 0-9 6 => 2026
message_1 = "This year is 2026"
match_obj = re.search("[0-9].[0-9][0-9]", message_1)
print(match_obj)

# special char [A-Z][a-z]
# r"" is raw string otherwise in consider /n as new line
str = r"Old/new"
pattern = "[A-Z][a-z][a-z].[a-z]"
# [A-Z] -O, . - /
match_obj = re.search(pattern,str)
print(match_obj)
# \d and \D \d matches 1 digit char similar to [0-9]
s1 = "Python3.14"
pat = r"[a-z][a-z][a-z]\d"
mobj = re.search(pat, s1)
# \D consider any char other than a digit
print(mobj)
pat = r"[a-z][a-z][a-z]\D"
mobj = re.search(pat, s1)
print(mobj)

# \s white space char and \n new line, \S any char with non space or new line
s2  = "PYthon 3.14"
pat2 = r"[a-z][a-z][a-z]\S"
mobj = re.search(pat2, s2)
print(mobj)

# \w - matches [A-Z][a-z][0-9]_
# \W - matches other then [A-Z][a-z][0-9]_
S3 = "PYThon_3@.14"
pat3 = r"\W\W"
mobj = re.search(pat3, S3)
print(mobj)