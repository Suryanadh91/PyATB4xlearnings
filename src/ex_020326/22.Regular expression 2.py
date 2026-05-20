import re

#sub() - substituting syntax => sub(pattern, replacement, string)
s1 = "Sunday, Monday, Tuesday, Sunday"
pattern = "sunday"
repalcement = "friday"
result = re.sub(pattern, repalcement, s1)
print(result)
# replace only 1 occurrence by using count
result = re.sub(pattern, repalcement, s1, count=1)
print(result)
# replace a day start with letter s only
pattern = r"S[a-z]+"
repalcement = "Friday"
result = re.sub(pattern, repalcement, s1)
print(result)
print("############################################")
s2 = """We are learning re. Using RE we can search for patterns in strings.
Using sub() we can replace the pattern with given string as well"""
pattern = "re"
replacement = "Regular Expression"
result = re.sub(pattern, replacement, s2)
print(result)
# we use boundary to replace only re not all words having re
pattern = r"\bre\b"
replacement = "Regular Expression"
result = re.sub(pattern, replacement, s2)
print(result)
# we use flags for replacing the uppercase RE also with flags=re.IGNORECASE
pattern = r"\bre\b"
replacement = "Regular Expression"
result = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)
print(result)
print("############################################")
phone_num = "+91-9494949449, 91-8099514045"
pattern = r"[+-]"
repalcement = ""
result = re.sub(pattern, repalcement, phone_num)
print(result)
print("############################################")
phones = "chinnu - 9494552084,surya - 8099514045,chinni - 9493307387"
pat = r"\d{10}"
complie_pat = re.compile(pat) # it complies and decreases the compile time when used multiple times
phn_num = re.findall(pat, phones)
print(phn_num)
ph_num = re.findall(complie_pat, phones)
print(ph_num)