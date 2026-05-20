# Continue - skips the below code and starts new iteration when the if condition is satisfied
# break - it terminates the loop when the condition is satisfied
for num in range(10):
    if num % 2 == 0:
        continue # skips the below code when num divisible by 2
    print(num)
print('##################################')
for number in range(1, 10):
    if number % 5 == 0:
        break # the range is 10 it terminates when condition satisfies
    print(number)
print('##################################')
# while loop - loop continues when it is true and terminates when it is false
num = 1
while num < 6:
    print(num)
    num = num + 1 # another way to right => num += 1
print('##################################')
correct_password = "Python"
while True: # infinite loop
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Password Correct")
        break
    else:
        print("Incorrect password")
print("Logged in successfully")
print('##################################')
import random
# # random module => import random => random.randint(), random, random.choice(),random.shuffle()
# # it gives a random number from 5 to 10 everytime we run  it
print(random.randint(5,10))
# # choice(sequence) => gives a random item from sequence
num = [10, 2 ,4, 6, 8, 15]
print(random.choice(num)) # gives a random item from list
fruits = ["apple", "banana", "cherry"]
random.shuffle(fruits) # direct print can't be used for shuffle function like choice function
print(fruits)
print('##################################')
# nested loops
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}") # for 1 iteration of 1st loop 2nd loop runs 2 iterations or 3 * 2 2nd loop runs 6 times
print('##################################')
# star pattern
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
print('##################################')
# Dice game

print("welcome to the game of rolling a dice")
while True: # runs infinite until we quit
    choice = input("press 'Enter' to roll or 'q' to quit.")
    choice = choice.strip() # to remove any extra space while entering
    if choice == 'q':
        print("Thanks for playing, goodbye")
        break
    elif choice == '': # empty to press enter
        number = random.randint(1, 6)
        print(f"your number is {number}")
    else:
        print("invalid input")
print("Game Over")
print('##################################')
# word count
# count countries start whith i
counter = 0
countries = ['india','russia','china','japan','usa','iran','africa','srilanka','iceland']
for country in countries:
    if country[0] == 'i':
        counter = counter + 1
print(counter)
# same code with startswith function and print country list
counter = 0
output = []
for country in countries:
    if country.startswith('i'):
        counter += 1
        output.append(country)
print(output)
print(counter)
print('##################################')
# deleting elements in dict, if we are running a loop on dict and trying to make change in dict it not possible
user = {
    'username': 'admin',
    'password': 'pasword123',
    'email': 'suryanadh@gmail.com',
    'address': 'kakinada',
    'country': 'India'}
sensitive_info = ["password","address"]
for i in sensitive_info:
    user.pop(i)
print(user)
# print('##################################')
# printing deleted key value pair
user = {
    'username': 'admin',
    'password': 'pasword123',
    'email': 'suryanadh@gmail.com',
    'address': 'kakinada',
    'country': 'India'}
sensitive_info1 = ["password","address"]

for i in sensitive_info1:
    if i in sensitive_info1:
        print(f"key:{i}, Value:{user[i]}")
        user.pop(i)
print(user)
print('##################################')
# trying to delete a element not present in the dict, code runs error free
user = {
    'username': 'Suryanadh',
    'password': 'Surya123',
    'email': 'suryanadh@gmail.com',
    'address': 'kakinada',
    'country': 'India'}
sensitive_info2 = ["password","address","phone"]

for i in sensitive_info2:
    if i in user:
        print(f"Deleted=> key:{i}, Value:{user[i]}")
        user.pop(i)
    else:
        print(f"{i} is not present in user, cannot delete")
print(user)
print('##################################')
import random
print("Welcome to the number guessing game")
print("The number lies between 1 to 50")
num = 1
attempts = 10 # to display no.of attempts left
secret_number = random.randint(1, 50)
is_guess_correct = False # extra function
while num <= 10: # to limit no.of in=terations to 10
    print(f"you have {attempts} attempts remaining.")
    user_num = int(input("Enter a number: "))
    if user_num == secret_number:
        print("congrats")
        is_guess_correct = True
        break
    else:
        if user_num < secret_number:
            higher_or_lower = "Higher"
        else:
            higher_or_lower = "Lower"
        print(f"wrong guess it is {higher_or_lower} number.")
    num = num + 1
    attempts -= 1
if is_guess_correct == False:
    print("Bad luck, try again")
print(f"The secret number is {secret_number}, Game over")
