# Quantifiers
import re

message = "The current Python version is 3.13 and older version is 3.04, 3.08, 3.10."

# "+" matches 1 or more repetitions of previous pattern
match_obj = re.search("[A-Z][a-z]+", message)
print(match_obj)

# "?" matches 0 or 1 repetitions of previous pattern
match_obj = re.search("[A-Z][a-z]?", message)
print(match_obj)

# "*" matches 0 or more repetitions of previous pattern
match_obj = re.search("[A-Z][a-z][a-z][a-z]*", message) # Need clarity
print(match_obj)

# {} we can mention the count by using the flower braces
match_obj = re.search("[A-Z][a-z]{5}", message)
print(match_obj)

# it checks for capital letter followed by 2 or 5 small letters
match_obj = re.search("[A-Z][a-z]{2,5}", message)
print(match_obj)
print("#"*50)
# Metacharacters

s1 = "Python is a programming language"
pat = r"[a-z]{8}"
match_obj = re.search(pat, s1)
print(match_obj)

# "^" caret checks the pattern from starting of the string
pat = r"^[a-z]{8}"
match_obj = re.search(pat, s1)
print(match_obj)

pat = r"^[A-z][a-z]{5}"
match_obj = re.search(pat, s1)
print(match_obj)


# "$" dollar checks the pattern from end of the string
pat = r"[a-z]{8}$"
match_obj = re.search(pat, s1)
print(match_obj)

# group - () matches the char mention inn the braces fully, "|" is used as or
emails = "suryanadh.com ranndom sivansh.edu"
pat = r"(com)|(edu)"
match_obj = re.search(pat, emails)
print(match_obj)

# Match finds matching at starting
s2 = "sivansh and sivaram are friends"
pat = r"[a-z]{5}"
match_obj = re.match(pat, s2)
print(match_obj)
print("#"*50)
# findall gets all the matches
phones = "Siva-9494552084, surya-8099514045, hari-9505666960, jai-123456789012, vishwam-123456789012345"
pat = r"[0-9]{10}"
match_obj = re.findall(pat, phones)
print(match_obj)
# phone min 10 digit max 12 digit
pat = r"[0-9]{10,12}"
match_obj = re.findall(pat, phones)
print(match_obj)
# we and boundary to filter valid which are 10 to 12 digits only
# so we add \b at start it count upto 12digits and \b at end it counts 12 digits from back so we get exact max 12 digit phn number
pat = r"\b[0-9]{10,12}\b"
match_obj = re.findall(pat, phones)
print(match_obj)
# phone min 10 digit and max all
pat = r"[0-9]{10,}"
match_obj = re.findall(pat, phones)
print(match_obj)
print("#"*50)
# finditer it gives iterator of matching objects
pat = r"[0-9]{10,}"
match_objs = re.finditer(pat, phones)
print(match_objs)
# to print the matching objects
for matches in match_objs:
    print(matches)