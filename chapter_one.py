
# FINDING THE MOST MENTIONED WORD **************

# varibale
hello = "hello world"
print("%s" % hello)

# list example
# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Accessing elements
first_number = numbers[0]  # Access the first element
second_number = numbers[1] # Access the second element

print("First number:", first_number)
print("Second number:", second_number)

# Modifying an element
numbers[2] = 10  # Changing the third element from 3 to 10
print("Modified list:", numbers)

# Adding a new element
numbers.append(6) # Adding a new element at the end
print("List after adding a new element:", numbers)

# function example - the varibles are the parameters
def add_numbers(number1, number2):
    result = number1 + number2
    return result



# module
from mdlu import greet 
greet("calvin")

# import counter to read words in sentence

from collections import Counter

# i need an input to store the sentence
text = "red is my favorite red red is amazing red"

# i want something to split my sentence into words
words = text.split()

print(words)

# i want somethign to count the amount of words repeat in the sentence

amount = Counter(words)
print(amount)

# ROBOT POISITION **************

# establish grid size 
grid_size = 6

# define the initial position of the robot
position = {'x': 0, 'y': 0}
direction = ''

# function to store the numberical value as the directions value is entered

def getsteps(steps):
    global direction, position
    if direction == 'up':
        position ['y'] += steps
    elif direction == 'down':
        position ['y'] -= steps
    elif direction == 'right':
        position ['x'] += steps
    elif direction == 'left':
        position ['x'] -= steps
    # lets make sure the robot stays in the grid. position stays in the grid parameters
    position['x'] = max(0, min(grid_size - 1, position['x']))
    position['y'] = max(0, min(grid_size - 1, position['y']))



direction = 'up'
getsteps(3)
direction = 'right'
getsteps(3)

print(position['x'], position['y'])


# COUNTING THE USER INPUT **************


# cound the numbers of words inputed by the user
print ("enter your sentence")
text = input()
textsep = text.split() 
textcount = len(textsep)


# now input a restriction of 80 total words
print ("enter your sentence")
text = input()
textsep = text.split() 
textcount = len(textsep)
if textcount > 80:
    print('your input is greater than 80 characters.')
else: print('your sentence contains ', textcount, " words")


# incorporate a loop to ask the user to re-enter the text
print ("enter your sentence")
text = input()
textsep = text.split() 
textcount = len(textsep)
if textcount > 80:
    print('your input is greater than 80 characters. Please try again')
else: print('your sentence contains ', textcount, " words")

# correct answer, however redundent IF statement, while itself is an IF statemnt

print('enter your sentence')
text = input()
textsep = text.split() 
textcount = len(textsep)

while textcount > 80:
    print('your input is greater than 80 characters. Please try again')
    text = input()
    textsep = text.split() 
    textcount = len(textsep)
    if textcount < 80:
        break

print('your sentence contains ', textcount, " words")


# cleaner version of the code

print('enter your sentence')
text = input()
textsep = text.split() 
textcount = len(textsep)

while textcount > 80:
    print('your input is greater than 80 characters. Please try again')
    text = input()
    textsep = text.split() 
    textcount = len(textsep)

print('your sentence contains ', textcount, " words")


# simpler soultion
print('enter your sentence')
text = input()
textcount = text.count(' ') + 1
print(textcount)


# CALCULATION USER INPUT ***********************

# ask the user to input one number, validate its actaully a number
# sucess

print('enter a number below')

while True:
    try:
        isnum = int(input())
        break
    except:
        print('this is not a number')

print('continue')

# now lets try to validate two numbers 
#sucess

print('enter your first number below')

while True:
    try:
        numone = int(input())
        break
    except:
        print('your first entry is not a number')

print('now enter your second number')
while True:
    try:
        numtwo = int(input())
        break
    except:
        print('your second entry is not a number')


print('both entries are numbers')

# more advance approach via CHATGPT.. one user input, one loop to validate

print('Enter two numbers separated by space:')

while True:
    try:
        # Take user input and split it into parts
        parts = input().split()

        # Expect exactly two parts
        if len(parts) != 2:
            raise ValueError("Please enter exactly two numbers")

        # Try converting each part to an integer
        # 0 references the list position of the first user input, 1 refernces the list position of the second user input
        numone = int(parts[0])
        numtwo = int(parts[1])

        # If successful, break out of the loop
        break
    except ValueError as e:
        # Print an error message
        print(f"Invalid input: {e}. Try again.")

print('Both entries are numbers:', numone, 'and', numtwo)



# continue problem
# now lets do an if statement to ensure number is less than 1000
print('enter your first number below')

while True:
    try:
        numone = int(input())
        break
    except:
        print('your first entry is not a number')

print('now enter your second number')
while True:
    try:
        numtwo = int(input())
        break
    except:
        print('your second entry is not a number')


print('both entries are numbers')

# validate if the product of both numbers is greather than 1000
numproduct = numone * numtwo
numsum = numone + numtwo

if numproduct <= 1000:
    print('your input can be multiplied', numproduct)
else:
    print('your entry was larger than 1000, thus we can only add them ', numsum )

# the soultion of the exercise

def mult_or_sum (num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
    
# first condition
result = mult_or_sum()
print('the resut is', result)
# second condition
result = mult_or_sum()
print('the result is', result)


# print the sum of the current number and the previous number ****************
# turn the input number into the range
print('input a number below')
numuser = input()
numint = int(numuser)
numrange = range(0,numint)
currentprev = 0

for n in numrange:
    currentn = n
    currentsum = currentn + currentprev
    print('your current position is ', currentn, 'your previous positoin is', currentprev, 'the sum is ', currentsum)
    currentprev = n


# learning python exercises #2 -- calculate volumn of cone *************************
# h & r is a number between 1 and 100. both are user input
# formula for volumn of cone (3.14*r^2*h)/3
# code the user input with the restrains
print('enter the radius value greater than 1 and less than 100')
while True:
    try:
        numone = int(input())
        if numone > 1 and numone < 100:
            break
        else:
            print('your number does not satisfy the range')
    except:
        print('your first entry is not a number')

print('now enter the height value greater than 1 and less than 100')
while True:
    try:
        numtwo = int(input())
        if numtwo > 1 and numtwo < 100:
            break
        else:
            print('your number is not within the range')
    except:
        print('your second entry is not a number')

r = numone
h = numtwo

volume = (3.14* r**2 * h)/3
print('your voulmn of your right cone is ', volume)

# numerical value determines the amount of o's in the string *************************
# the value of s = the amount of o's in the string
print('enter a value for the amount of o\'s in the string')
spooky = int(input())
string = "o" * spooky
print('sp' + string + 'ky')

# far far away exercise *************************
farinput = int(input()) - 1
farnum = 'far, ' * farinput
lastfar = 'far'
print('a long time ago in a galaxy ' + farnum + lastfar + ' away')

# using a while loop to validate the inputs for exervise above
print('enter a number between 1 and 5')
while True:
    farinput = int(input())
    if farinput > 0 and farinput <= 5:
        break
    else:
        print('please enter a number between 1 and 5')
    
if farinput > 1 and farinput <= 5:
    farlimit = farinput - 1
    farnum = 'far, ' * farlimit
    print('a long time ago in a galaxy ' + farnum + 'far away')
else:
    if farinput == 1:
        print('a long time ago in a galaxy far away')
    else:
        print('please enter a number between 1 and 5')


# QUICK PYTHON EXERCISES ******************
# exercise 1: output a string with specific indentation 
poem = 'Twinkle, twinkle, little star \n How I wonder what you are! \n Up above the world so high, \n Like a diamon in the sky. \n Twinkle, twinkle, little star, \n How I wonder what you are'

# split the poem, not by spaces, but by \n
poemsplit = poem.split('\n')
# print(poemsplit)
indentamount = " " * 3
indentamount2 = " " * 4
# lets code line by line
poemline1 = indentamount + poemsplit[1]
poemline2 = indentamount2 + poemsplit[2]
poemline3 = indentamount2 + poemsplit[3]
poemline4 = indentamount + poemsplit[5]


# chatGPT alternative code - Advance level code
# code below represents the poem line indent code. for each mentioned position of poemsplit, assing it a number 
poem = 'Twinkle, twinkle, little star \n How I wonder what you are! \n Up above the world so high, \n Like a diamon in the sky. \n Twinkle, twinkle, little star, \n How I wonder what you are'
poem_lines = poem.split('\n')

# Example: Dictionary mapping line indices to their indentation levels
indent_levels = {1: 3, 2: 4, 3: 4, 5: 3}

# Apply indentation
for i, line in enumerate(poem_lines):
    indent = " " * indent_levels.get(i, 0)  # Default to 0 if line number not in dict
    poem_lines[i] = indent + line

# Join and print the final poem
formatted_poem = '\n'.join(poem_lines)
print(formatted_poem)


# function to output the multiple of two numbers ******************
def countbynum (number1, number2):
    countlist = [] # empty list
    for n in range(1, number2 + 1): # range starts at 1, ends at number2 + 1
        countlist.append(n * number1) # append/update the list with the product of n and number1
    return countlist # return the list
    
numoutput = countbynum(2, 5)
print(numoutput)

# advance code for the exercise above
def countbynum (number1, number2):
    return [n * number1 for n in range(1, number2 + 1)] # list comprehension
print(countbynum(2, 5))



# new list is created with random letters from the list of letters **************

import random
letters = ['G', 'C', 'A', 'T'] # list of letters
random_letters = [letters[random.randrange(len(letters))] for i in range(10)] # list comprehension, for loop is amount of times it runs, random.randrange(len(letters)) is the random number generator, len(letters) is the length of the list, outisde [] is the new list
print(random_letters)
random_letters_word = "".join(random_letters) # join() method takes all items in an iterable and joins them into one string.
print(random_letters_word)
random_letters_r = random_letters_word.replace('T', 'U') # replace() method replaces a specified phrase with another specified phrase.
print(random_letters_r)

# function to convert dna to rna

def dna_to_rna(dna):
    if dna == '': # if the DNA sequence is empty, return an empty string
        return dna
    else:
        rna = dna.replace('T', 'U')
        return rna # return the RNA sequence instead of printing it
  
    
dna_sequence = 'AGTTCTTAAT' # DNA sequence
rna_sequence = dna_to_rna(dna_sequence) # RNA sequence
print(f'"{dna_sequence}" => "{rna_sequence}"')

# optimized code
def dna_to_rna(dna):
    # Check if the DNA sequence is non-empty
    if dna: # if dna does not equal '', truthy value
        return dna.replace('T', 'U')
    else:
        # Return the empty string directly becuase dna is empty
        return dna

# Example usage
dna_sequence = 'AGTTCTTAAT'  # DNA sequence
rna_sequence = dna_to_rna(dna_sequence)  # RNA sequence
print(f'"{dna_sequence}" => "{rna_sequence}"')


# two functions calculation for varible values ******************
numyoung = 0
nummiddle = 0


def young (age):
    global numyoung
    if age >= 0 and age <= 50:
        numyoung = age
        return numyoung
    else:
        return 0

def middle (age):
    global numyoung, nummiddle
    if age >= numyoung and age <= 50:
        nummiddle = age
    else:
        return 0
    
young(12)
middle(15)
print(numyoung)
print(nummiddle)
numold = (nummiddle - numyoung) + nummiddle
print(numold)

# advance code for the exercise above
def calculate_ages(youngest_age, middle_age):
    if youngest_age < 0 or middle_age < 0:
        return "Error: Age cannot be negative" 

    if 0 <= youngest_age <= 50 and youngest_age <= middle_age <= 50: 
        oldest_age = (middle_age - youngest_age) + middle_age
        return youngest_age, middle_age, oldest_age
    else:
        return "Error: Invalid age range"

# Example usage
youngest = 12
middle = 15
ages = calculate_ages(youngest, middle)

# only output the oldest age if there is no error
# Check if the function returned an error message
if isinstance(ages, str): # if ages is a string, then ages is an error message
    print(ages)
else:
    # Unpack the tuple to get the oldest age
    _, _, oldest = ages # _ means we don't care about the value
    print("Oldest age:", oldest)

# function to return an interger from a string ******************
def str_to_int(word): # codewars gives me an error b/c they want a specific name for the function
    return int(word) # its good practice to retrun the value instead of printing it
str_to_int("1234")

# function to return string based on value ******************
def bmi (weight, height):
    bmi =  weight / height ** 2
    if bmi <= 18.5:
        return "underweight"
    elif bmi <= 25:
        return "normal"
    elif bmi <= 30:
        return "overweight"
    else:
        return "obese"
    
print(bmi(80, 1.8))

# function for liters per hour ******************
import math
water = 0.5 #liters per hour

def litres (time):
    amount =  water * time
    return math.floor(amount)


print(litres(3))

# advance code for the exercise above
def litres(time):
    return time // 2

# calculate rate of pay with overtime ******************
hourstrng = input()
hoursint = float(hourstrng)
ratestrng = input()
rateint = float(ratestrng)
if hoursint > 40:
    pay = 40 * rateint + (hoursint - 40) * rateint * 1.5 # 1.5 times the hourly rate for hours worked above 40 hours
else:
    pay = hoursint * rateint

print(pay)

# else if statement exercise ******************
student = input('Enter your score: ')
score = float(student)
if score < 0.0 or score > 1.0:
    print('Error')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')


# library to solve for an equation ******************
from sympy import symbols, Eq, solve

# Define the symbol
y = symbols('y')

# Define the equation
equation = Eq(y + 10, 20)

# Solve the equation
solution = solve(equation, y)
print(solution)

# exercise to demonstrate the use of the library above
from sympy import symbols, Eq, solve

cinput = int(input()) # input will be between -40 and 40

celsius = cinput

fahrenheit = symbols('fahrenheit')

equation = Eq((celsius * 9/5) + 32, fahrenheit)

fahrenheit_value = int(solve(equation, fahrenheit)[0]) # removes the decimals from the answer

print(fahrenheit_value)

# passing a user input to a function ******************
def add_numbers(a, b):
    # Perform some calculation with the arguments
    return a + b

# Prompting for user input outside the function
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Calling the function with user input as arguments
result = add_numbers(first_number, second_number)
print(f"The result of adding {first_number} and {second_number} is {result}.")

# example of a function passing a user input
def computepay(h,r):
    if h > 40:
        pay = 40 * r + (h - 40) * r * 1.5 # 1.5 times the hourly rate for hours worked above 40 hours
    else:
        pay = h * r
    return pay

hrsinput = input("Enter Hours:")
hrsint = float(hrsinput)
rateinput = input("Enter Rate:")
rateint = float(rateinput)
p = computepay(hrsint,rateint)
print(p)


# function with while loop and list ******************
userlist = [] # empty list, intialize before the loop
largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done": # check for the sentinel value, if true, break out of the loop
            break
        else:
            isnum = int(num)
            userlist.append(isnum)
    except:
        print("Invalid input")
        continue

largest = max(userlist)
smallest = min(userlist)
print("Maximum is", largest)
print("Minimum is", smallest)

# function to determine baskeball winner, global vs local varible ******************
# why my version didnt work
'''The issue you're encountering is due to the scope of the variables atotal and btotal. 
The atotal inside the function apple_score is a local variable, meaning it only exists within the function's scope. 
When you assign a value to atotal inside the function, it doesn't affect the global atotal defined at the start of your code.'''

atotal = 0
btotal = 0

def apple_score (a,b,c):
    atotal = (a*3)+(b*2)+(c*1)
    return atotal

def banna_score(a, b, c):
    btotal =  (a * 3) + (b * 2) + (c * 1)
    return btotal

apple_score(10, 3, 7)
print(atotal)

# the correct version
def apple_score (a,b,c):
    return (a*3)+(b*2)+(c*1)

def banna_score(a, b, c):
    return (a * 3) + (b * 2) + (c * 1)

atotal = apple_score(10, 3, 7)
btotal = banna_score(8, 9, 6)

if atotal > btotal:
    print("Apple wins!")
elif atotal < btotal:
    print("Banna wins!")
else:
    print("It's a tie!")

# chatgpt version of the exercise above - create one function to calculate the score
def calculate_score(three_pointers, two_pointers, free_throws):
    return (three_pointers * 3) + (two_pointers * 2) + (free_throws * 1)

# refernce the function twice to calculate the score for each team
apple_score = calculate_score(10, 3, 7)
banna_score = calculate_score(8, 9, 6)

# multiple if statements are treated independently, else if statements are treated as one

# if statement with multiple conditions ******************
# my code below
print('Enter a 4 digit phone number, seperated by (-):')
phone = input()
phone_split = phone.split('-') # split the phone number into a string list

# analyze the one time phone number
if int(phone_split[0]) in range(8, 10) and int(phone_split[3]) in range(8, 10) and int(phone_split[1]) == int(phone_split[2]):
    print('telemarketer, dont answer')
else:
    print('answer')

# chatgpt version of the exercise above, however there is no loop to ask the user to re-enter the phone number
print('Enter a 4 digit phone number, separated by dashes (e.g., 8-1-1-9):')

try:
    phone = input()
    phone_split = phone.split('-')  # split the phone number into a string list

    if len(phone_split) != 4:
        raise ValueError("Please enter exactly four digits separated by dashes.")

    # Convert all segments to integers and store them in a list
    digits = [int(segment) for segment in phone_split]

    # use parenthesis to make the if statement more readable and determine order of operations
    if (digits[0] == 8 or digits[0] == 9) and \
       (digits[1] == digits[2]) and \
       (digits[3] == 8 or digits[3] == 9):
        print('Telemarketer, dont answer')
    else:
        print('Answer')
except ValueError as e:
    print(f"Invalid input: {e}")

# loop iteration to ask user to re-enter the phone number
while True:
    try:
        print('Enter a 4 digit phone number, separated by dashes (e.g., 8-1-1-9):') # ask the user to enter a phone number inside the loop
        phone = input()
        phone_split = phone.split('-')

        if len(phone_split) != 4:
            print("Please enter exactly four digits separated by dashes.")
            continue

        digits = [int(segment) for segment in phone_split] # convert all segments to integers and store them in a list
        if (digits[0] == 8 or digits[0] == 9) and (digits[1] == digits[2]) and (digits[3] == 8 or digits[3] == 9): # use parenthesis to make the if statement more readable and determine order of operations
            print('Telemarketer, don\'t answer')
            break
        else:
            print('Answer')
            break

    except ValueError: # if the user enters a non-integer value, ValueError will be raised
        print("Invalid input. Please ensure you enter numbers.") # print an error message and continue the loop
    

# multiple functions and summing them ******************
def burger_choice(choice):
    if choice == 1: # cheeseburger
        return 461
    elif choice == 2: # fish burger
        return 431
    elif choice == 3: # veggie burger
        return 420
    else:
        return 0
    
def side_choice(choice):
    if choice == 1: # fries
        return 100
    elif choice == 2: # baked potato
        return 57
    elif choice == 3: # chef salad
        return 70
    else:
        return 0
    
def drink_choice(choice):
    if choice == 1: # soft drink
        return 130
    elif choice == 2: # orange juice
        return 160
    elif choice == 3: # milk
        return 118
    else:
        return 0

def dessert_choice(choice):
    if choice == 1: # apple pie
        return 167
    elif choice == 2: # sundae
        return 266
    elif choice == 3: # fruit cup
        return 75
    else:
        return 0

total_calories = burger_choice(int(input())) + side_choice(int(input())) + drink_choice(int(input())) + dessert_choice(int(input()))
print("Your total Calorie count is " + str(total_calories) + ".")

# date function, user input function, and if statement ******************
# lets import datetime
import datetime


# we do not need a dictionary, we can just use the datetime tools
# my_dict = {1: 'jan', 2: 'feb', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'aug', 9: 'sept', 10: 'oct', 11: 'nov', 12: 'dec'}

# lets create a function that will accept two varibles
def create_date(month_num, day_num): # pass two varibles to the function
    year = 2023 # set the year
    return datetime.date(year, month_num, day_num) # return the date, the datetime will convert the month_num to the month name and the day_num to the day number. 

# lets accept a user input
# lets validate the user input
while True:
    try: # try is the happy path
        month_input = int(input('Enter a month in single digit format: ')) # ask the user for a date in the format of a single digit
        day_input = int(input('Enter a day in single digit format: ')) # ask the user for a day in the format of a single digit
        # lets create a varible that will call the function
        user_date = create_date(month_input, day_input) # pass the two varibles to the function
        break # break the loop if no ValueError occurs
    except ValueError: # if a ValueError occurs, the except will run
        print("Invalid input. Please enter a valid date.")

# now lets compare the date 

feb_date = create_date(2, 18) # create a varible that will call the function for specific date

if user_date == feb_date: # if the user_date is the same as feb_date
    print('Happy Birthday!') # print Happy Birthday
elif user_date > feb_date:
    print('After')
else:
    print('Before') 

# counter and reference spefic key in dictionary ******************
from collections import Counter

# i need an input to store the sentence
text = ":-) i am happy :-) but at times i am sad :-("

# i want something to split my sentence into words
words = text.split()

print(words)

# i want somethign to count the amount of words repeat in the sentence

amount = Counter(words) # counter creats a dictionary of words and their counts

happy = ':-)' # happy face is present in the counter dictionary, so it can be referenced as a key via [happy]
sad = ':-(' # sad face is present in the counter dictionary, so it can be referenced as a key via [happy]

if amount[happy] > amount[sad]:
    print("happy")
elif amount[happy] < amount[sad]:
    print("sad")
else:
    print("unsure")

# sort user input, for statement, strip, split & isdigit ******************

num = input("Enter numbers seperated by commas: ")
order = input("Enter asc or desc: ")

# lets create a function that will accept two varibles but validate the input
def num_sort(num,order):
    try:
        num_list = [int(n) for n in num.split(",") if n.strip().isdigit()] # the for loop will run through each instance and the IF statement will check if it is a digit. the result will be placed in a list. 
    # validate the list contains the same number of items as the original string
        if len(num_list) != len(num.split(",")):
            raise ValueError ("inputs contains non-numeric characters") # the if statement catches non-numeric characters and raises an error
        
        if order == "asc":
            num_split = num.split(",")
            num_sort = sorted(num_list)
            return num_sort
        elif order == "desc":
            num_split = num.split(",")
            num_sort = sorted(num_list, reverse=True)
            return num_sort
        else:
            return ("invalid input for order") # catches invalid input for order
    except ValueError as err: # catches invalid input for num, however, is.digit() will catch non-numeric characters. this is an extra layer of protection
        return f"Invalid input: {err}"

print(num_sort(num,order))


# decimal in programming refers to the base-10 number system exercise *********
while True:
    try:
    # converting a decimal (base of 10) number to binary
        usernum = float(input("Enter decimal number: ")) # input needs to be turned into a float(float accepts deciamls),
        mathnum = bin(int(float(usernum)))
        print(mathnum)
        break
    except ValueError as bad: # catches word in place of number
        print(f"bad input: {bad}")
# the ValueError is a type of exception that is raised when an operation or function 
# receives an argument that has the right type but an inappropriate value, 
# and it needs to be caught in a try-except block.


# count() refernce a list of words in a sentence exercise ******************

# The .count() method on a string object is used to count the occurrences of a substring within the string, 
# not individual characters.
# turning the list into a string, then using the count() method on the string will see the values as a whole, not individual characters
'''
vowels = ['a', 'e', 'i', 'o', 'u'] # list of letters i am looking for in a sentence
my_string = ''.join(vowels) # convert list to string so i may use a count() method (count() method only works on strings)
sentence = 'hi my name is calvin, how are you' # sentence to search
lowercase = sentence.lower() # convert sentence to lowercase
vword = lowercase.count(my_string) 
print(vword) # print the number of times the vowels appear in the sentence
'''

# i want to see each instance in the list, not the total number of instances. Thus, I need to search for each letter individually

vowels = ['a', 'e', 'i', 'o', 'u'] # list of letters i am looking for in a sentence
sentence = 'hi my name is calvin, how are you' # sentence to search
lowercase = sentence.lower() # convert sentence to lowercase
vword = 0 # set the counter to 0 for my loop

for i in vowels: # loop through each letter in the list
    vword += lowercase.count(i) # add the number of times each letter appears in the sentence to the counter
    print(i, lowercase.count(i)) # print the letter and the number of times it appears in the sentence

# function example
vowels = ['a', 'e', 'i', 'o', 'u'] # list of letters i am looking for in a sentence
def count_vowels(word): # define a function to count the vowels
    lowercase = word.lower() # convert sentence to lowercase
    vword = 0 # set the counter to 0 for my loop
    for i in vowels: # loop through each letter in the list
        vword += lowercase.count(i) # add the number of times each letter appears in the sentence to the counter
        print(i, lowercase.count(i)) # print the letter and the number of times it appears in the sentence

sentence = input('enter a sentence: ') # sentence to search
count_vowels(sentence) # call the function


# credit card function - slice string at specific amount exercise ********************
# ask the user to input a credit card number

def get_cc(cc):
    while True:
        try:
            if not cc.isdigit(): # i can check only for integers with isdigit() without needing to turn the input into an integer
                raise ValueError("only input digits")
            elif len(cc) != 16:
                print('enter only 16 digits')
            else: # slice the string based on a starting position
                cc_user = cc[-4:] # the -4 is the starting point of where you want to slice the string
                return cc_user
                break
        except ValueError as bad:
            print(f"bad input: {bad}")

cc = input('enter your 16-digit number: ')
print(get_cc(cc))


# dictionary rock paper scissors exercise **********************

# paper beats rock / paper looses to scissors
# rock looses to paper / rock beats scissors
# scissors looses to paper / scissors beats paper   
# create a dictionary where the keys are the choses (left side) and values is what they beat (right side)

rules = {'paper': 'rock',
         'rock': 'scissors',
         'scissors': 'paper'
         }

def rps(p1,p2):
    if p1==p2:
        return 'its a tie'
    elif rules[p1] == p2: # rules[p1] looks for the value associated to the key (user input of scissors, rock or paper) then it returns the value. if the value matches what p2 enters, then we know player 1 won
        return 'player 1 won!'
    else:
        return 'player 2 won'

    
