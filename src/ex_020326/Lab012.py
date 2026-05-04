# For and while loop
# sequence = list,tuple,dict,string,etc
# for var in sequence:
# for lop for Dict
emp = {'id':2574, 'name':'Surya', 'dep':"Testing"}
for details in emp:
   # print(details) # prints only keys
   # print(emp[details]) # prints only values
    print(details, emp[details]) # prints both keys and values
# items keyword gets the all items from dict as tuple
print('################################')
for details in emp.items():
    print(details) # print all items as tuple
print('################################')
for details in emp.items():
    print(details[0]) # print only keys
print('################################')
for details in emp.items():
    print(details[1]) # print only values
print('################################')
for details in emp.items():
    print(details[0],details[1]) # print keys and values
print('################################')
# Range function it generate sequence of integers
# syntax- range(start, stop, step), range(start, stop) by default step is 1, range(stop) default start = 0 and stop is stop-1
# gives numbers 1 to 10
for i in range(1, 11, 1):
    print(i)
print('################################')
# gives even numbers
for i in range(2, 11, 2):
    print(i)
print('################################')
# reverse order 20 to 10
for i in range(20, 9, -1):
    print(i)
print('################################')
for i in range(1, 6):
    print(i)
print('################################')
for i in range(6):
    print(i)
print('################################')
profits = [9, 11, 8, 12]
for index in range(len(profits)):
    q = index + 1
    print(f"profit in quarter {q} is {profits[index]}")
print('################################')
scores = [50, 2, 51, 21, 61, 101, 33, 0, 4, 6, 12]
total_score = 0
for score in scores:
    total_score = total_score + score
print(f"total score is {total_score}")

# using sum function
total_score = sum(scores)
print(f"total score is {total_score}")
print('################################')
highest_score = scores[0]
for score in scores:
    if highest_score < score:
        highest_score = score
print(f"highest score is {highest_score}")

lowest_score = scores[0]
for score in scores:
    if score < lowest_score:
        lowest_score = score
print(f"lowest score is {lowest_score}")
print('################################')
# using max(), min() function
highest_score = max(scores)
print(f"highest score is {highest_score}")
lowest_score = min(scores)
print(f"lowest score is {lowest_score}")
print('################################')