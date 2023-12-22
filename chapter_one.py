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


# COUNTING THE USER INPUT EXERCISE **************


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


# CALCULATION USER INPUT EXERCISE ***********************

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


# print the sum of the current number and the previous number EXERCISE ****************
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


# learning python exercises #2 -- calculate volumn of cone  EXERCISE *************************
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

# numerical value determines the amount of o's in the string EXERCISE *************************
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


# function to output the multiple of two numbers EXERCISE ******************
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



# new list is created with random letters from the list of letters EXERCISE **************

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


# two functions calculation for varible values EXERCISE ******************
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

# function to return string based on value EXERCISE ******************
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

# function for liters per hour EXERCISE ******************
import math
water = 0.5 #liters per hour

def litres (time):
    amount =  water * time
    return math.floor(amount)


print(litres(3))

# advance code for the exercise above
def litres(time):
    return time // 2

# calculate rate of pay with overtime EXERCISE ******************
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


# library to solve for an equation EXERCISE ******************
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

# passing a user input to a function EXERCISE ******************
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


# function with while loop and list EXERCISE ******************
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

# function to determine baskeball winner, global vs local varible EXERCISE ******************
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

# if statement with multiple conditions EXERCISE ******************
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
    

# multiple functions and summing them EXERCISE ******************
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

# date function, user input function, and if statement EXERCISE ******************
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

# counter and reference spefic key in dictionary EXERCISE ******************
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

# sort user input, for statement, strip, split & isdigit EXERCISE ******************

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

    
# if elif, subtraction operator
# my version
def rental_car_cost(d):
    if d >= 7:
        cost = (d*40) - 50
    elif d >= 3 and d < 7:
        cost = (d*40) - 20
    else:
        cost = d*40
    return cost

print(rental_car_cost(4))

# alt version
def rental_car_cost(d):
    result = d * 40 # establish the varaible
    if d >= 7:
        result -= 50 # based on the result, -= is subtracing from total
    elif d >= 3:
        result -= 20 
    return result # no need for else statement


# array, list of strings and integers turn into a list of integers exercise **********************

# Given an array of integers as strings and numbers, (complete)
# return the sum of the array values as if all were numbers. (complete)
# Return your answer as a number. (complete)
# provide function



def sum_mix(arr): # pass an array of integers as strings and numbers
    for i in range(len(arr)): # loop through the array with range of length of array
        arr[i] = int(arr[i]) # convert the array to integers
    return sum(arr) # return the sum of the array values as if all were numbers

arr = [5, '3', 6, '7'] # array of integers as strings and numbers
print(sum_mix(arr)) # pass the array to the function and print the result
    

# using map() below
def sum_mix(arr):
    return sum(map(int, arr)) # map() applies the int() function to each element of the array


# using absolut value to find a negative number
# using if statement to find negative number
def make_negative( number ):
    if number >= 0:
        return number*-1
    elif number < 0:
        return number
    
# using abosulte value to find negative number

def make_negative( number ):
    return -abs(number)

# slope formula function exercise **************************
# slope formula = (y2 - y1)/(x2 - x1)

# function method

def cal_slope(point1, point2):
    return (point2[1] - point1[1])/ (point2[0] - point1[0])

point1 = (2,2)
point2 = (6,4)

slope = cal_slope(point1,point2)

print(slope)

# for loop output in same line, adding + to each instance exercise ********************
# receive a number -- find the sum of the number from 1 to Num
# number will always be postive > 0
# math formula --> s = n(n + 1)/2
# example: 8 --> 36(total sum)(complete) (1+2+3+4+5+6+7+8)(breakdown)


num = 8

total = num*(num + 1)/2
print(total)

for i in range(1, num+1):
    if i < num:
        print(i, end='+')
    else:
        print(i)

# no if statement
num = 8

total = num*(num + 1)/2
print(total)

for i in range(1, num): # run the for loop from 1 to 7 (num - 1)
    print(i, end='+') # it will add a + from 1 to 7
print(num) # print the num (8) and it will achieve the same result


# for loop end='' to print on same line exercise **********************

# example: 8 --> 36(total sum)(1+2+3+4+5+6+7+8)(for loop with parenthesis)


def summation(num):
    total = num * (num + 1) // 2
    print(total, '(', end='') # end='' to print on the same line and add a parenthesis
    for i in range(1, num + 1):
        if i < num:
            print(i, end='+') # end='+' to add a plus sign
        else:
            print(i, end=')') # end=')' to add a closing parenthesis
    return total # function should always include a return


# capitilization of first & last letters only vs using for loop *************************
# capitalize function
def abbrev_name(name):
    full = name.split()
    first = full[0]
    last = full[1]
    first_letter = first[:1].capitalize() # get initial of first name and capitalize it
    last_letter = last[:1].capitalize() # get initial of last name and capitalize it
    return f"{first_letter}.{last_letter}"

print(abbrev_name('calvin broadus'))

# for loop example
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
    # w will look for the first letter in the name.split().upper() and join a dot. after it


# enumrate() list comprehension exercise **********************
# integers
string_num = input('enter numbers seperated by space: ') # enter numbers seperated by space
# string_num_split = string_num.split(), no need for this varible, as my list comprehension will reference it
# num_list = [] # the new list that will contain the new int values

# traditional method
'''
for n in string_num_split:
    num_list.append(int(n)) # convert each instance into integers, by appending the new list
'''
    
# list comprehension
num_list = [int(n) for n in string_num.split()] # setting up the new list with the for loop

# now create a threshold to replace any number below this amount
threshold = 5


# this is wrong, [n] is not part of num_list, however, my code is programed as it is
'''
for n in num_list:
    if num_list[n] > threshold:
        num_list[n] == 0
print(num_list)
'''

# use enumrate() to find the index and the elemeant at that specific index
for index, value in enumerate(num_list):
    if value > threshold: # if the value (element) is greater than the threshold, replace it with 0 (zero
        num_list[index] = 0 # replace the value at that index with 0 (zero)
print(num_list)

# replacing user input string with char, for loop, replace() exercise **********************
stringnum = input("Enter numbers: ")
# stringnum_five = stringnum.__contains__("5") # i can use 5 in method

'''
if "5" in stringnum: # i can check 5 in stringnum
    stringnum = stringnum.replace("5", "0")
    print(stringnum)
else:
    print(stringnum)
'''

for char in stringnum:
    if char > "5":
        stringnum = stringnum.replace(char, "1")
    elif char < "5":
        stringnum = stringnum.replace(char, "0")

print(stringnum)

# use a new string, vs updating the original string with the replace() method for the exercise above

def fake_bin(stringnum):
    new_string = "" # new_string will be the new string that will be returned
    for char in stringnum:
        if char >= "5":
            new_string += "1"
        elif char < "5":
            new_string += "0"
    return new_string


stringnum = input("Enter numbers: ")
print(fake_bin(stringnum))


# accept INT - convert to string - convert back to int exercise **************

# given an integer input, sqaure each instance of the input
# no seperators, given integer, return integer

user_num = int(input())
print(user_num)

# convert int input into a string

user_str = str(user_num)
print(type(user_str))

# now that its a string, i want to reference each input

for char in user_str: # it will run through each input
    add = int(char) + 2 # converts stg input back to int with math operator
    print(add)

# square root example

for char in user_str: # it will run through each input
    sqaure = round(int(char) ** 0.5) # converts stg input back to int, square roots by raising it to 0.5
    print(sqaure)

# function example

# below function will ouput the final result in int using it as a string

def square_digits (num):
    num_stg = str(num)
    result = "" # this will store each iteration value
    for char in num_stg:
        square = round(int(char) ** 0.5)
        result += str(square) # to store each iteration, but need to turn it back to a str
    return int(result) # return the final output in integer
user_num = int(input())

print(square_digits(user_num))

# more efficient method using list
def square_digits (num):
    num_stg = str(num)
    result = [] # turn to list
    for char in num_stg:
        square = round(int(char) ** 2)
        result.append(str(square)) # to store each iteration, but need to turn it back to a str
    return int(''.join(result)) # return the final output in integer

user_num = int(input())

print(square_digits(user_num))



# list/dict/for loop/any()/dict.value() exercise ***********************

user_input = 'hello'
input_list = [char for char in user_input] # establish the for loop instance as the list value for each loop
print(input_list)
intput_dic = {x: input_list.count(x) for x in input_list} # x is the for loop instance, count(x) refernces how many times x shows up in the list, for x in list is the loop, all inside a dictionary for a key and a value
# intput_dic.values() returns the values of my dict
# any() is a boolean that accpets a iterable/list/generator
if any(x > 2 for x in intput_dic.values()): # asking if boolean if x (foor loop instance) is greater than 2 within my dict value function
    print('nope')
else:
    print('yep')




'''
for loop used for input_list comprehension
if i want to print each instance, keep the for loop

for char in user_input:
    input_list.append(char)
    print(input_list)
'''

# function example for above
def is_isogram(string):
    lower_string = string.lower() # ignore sensitve cases
    input_list = [char for char in lower_string] # establish the for loop instance as the list value for each loop

    intput_dic = {x: input_list.count(x) for x in input_list} # x is the for loop instance, count(x) refernces how many times x shows up in the list, for x in list is the loop, all inside a dictionary for a key and a value

    if any(x >= 2 for x in intput_dic.values()): # asking if boolean if x (foor loop instance) is greater than 2 within my dict value function
        return False
    else:
        return True

print(is_isogram('heLlo'))


# more practice on list, & for loops exercise ************************

user_input = 'hello'
user_input_lower = user_input.lower() 
user_input_list = [char for char in user_input_lower]
print(user_input_list)
letter_list = ['a', 'e', 'i', 'o', 'u']
letter_count = 0
print(letter_list)


for x in user_input_list:
    if x in letter_list:
        letter_count += 1

if letter_count == 0:
    print('no vowels in the input')

print(letter_count)

# line vs char for loops new line EXERCISE **************************
# This loop prints each character in the string
for char in "Hello, world!":
    print(char)

# This loop prints each line in the file
with open("some_file.txt") as file:
    for line in file:
        print(line)


# want to read a char instead of a line within  a file

# Open the file
with open("some_file.txt") as file:
    # Read the entire file into a string
    content = file.read()

# Initialize a counter
char_count = 0

# Iterate over each character in the string
for char in content:
    # Increment the counter
    char_count += 1

# Print the total character count
print(char_count)

# open, read, with method file handeling exercise **************
# simple method
text = open('/Users/calvinpineda/Downloads/words.txt','r')
text_content = text.read()
print(text_content)
text.close()

# recommended method
# use with method
# with method ensures the file is closed once complete
with open('/Users/calvinpineda/Downloads/words.txt','r') as file:
    contents = file.read()

print(contents)


# scripting/extracting specific value exerise not finished EXERCISE *****************


line_num = 0 # used to determine which exact line the text is found
# target_num = 45
with open('/Users/calvinpineda/Downloads/mbox-short.txt','r') as file:
    # contents_find = contents.find('X-DSPAM-Confidence:    0.8475')
    '''for x in file:
        line_num += 1
        if line_num == 45:
            print(f"Line {line_num}: {x}")
            break
    
    '''
    for x in file:
        line_num += 1 # so i can store which line stores the startwith
        if x.startswith('X-DSPAM-Confidence:'):
            print(f"Line {line_num}: {x}") # remove break to return every isntance of the startwith line
    
# trying to extract the decimal value
line_num = 0 # used to determine which exact line the text is found
line_store = []
with open('/Users/calvinpineda/Downloads/mbox-short.txt','r') as file:
    for x in file:
        line_num += 1 # so i can store which line stores the startwith
        if x.startswith('X-DSPAM-Confidence:'):
            line_store = [x.rstrip()]
            print(f"{x}") # remove break to return every isntance of the startwith line
            print(line_store)

# correct answer for above


# line_store = []
line_sum = []
with open('/Users/calvinpineda/Downloads/mbox-short.txt','r') as file:
    for x in file:
        if x.startswith('X-DSPAM-Confidence:'):
            non_space = x.strip()
            line_split = non_space.split(':')
            # line_store = [float(line_split[1])] # after append, this becomes redudundent
            # line_sum += line_store # I am extending the list via +=, rather, i can store the number itself in the line_sum list
            line_sum.append(float(line_split[1]))
            print(float(line_split[1]))
line_cal = sum(line_sum)/len(line_sum)
print(line_cal)

# updated to answer the specific exercise
line_sum = []
line_count = 0
line_total = 0
with open('/Users/calvinpineda/Downloads/mbox-short.txt','r') as file:
    for x in file:
        if x.startswith('X-DSPAM-Confidence:'):
            line_count += 1
            non_space = x.strip()
            line_split = non_space.split(':')
            line_sum.append(float(line_split[1]))
            line_total += float(line_split[1]) # keep a running total
line_cal = line_total/line_count
print('Average spam confidence: ',line_cal)



# split words and checking if already exist exervise ******************

line_store = []
with open('/Users/calvinpineda/Downloads/romeo.txt','r') as file:
    for x in file:
        split_line = x.split() # checking each word
        for z in split_line:
            if z in line_store:
                continue
            else:
                line_store.append(z) # if not present, add it to single list
print(line_store)

# using a set() for the exercise above
# use a set, as a set can be added an element, but it cannot change. 
line_store = set()
with open('/Users/calvinpineda/Downloads/romeo.txt','r') as file:
    for x in file:
        split_line = x.split() # checking each word
        for z in split_line:
            line_store.add(z) # if its not present, it will be added. if its, nothing will change
print(list(line_store))

# extracting data from line exercise ***********************************

x_count = 0
with open('/Users/calvinpineda/Downloads/mbox-short.txt','r') as file:
    for x in file:
        if x.startswith('From:'):
            x_list = x.split()
            x_count += 1
            print(x_list[1])
    print(x_count)


# converting input into list - list(input()) vs [input()]


# user_list = [input()] this gets the entire input as one string and puts it into a list
user_list = list(input()) # gets input and seperates into a list

user_list_num = []

for x in user_list:
    user_check = x.isdigit()
    if user_check == True:
        user_list_num.append(x)

print(user_list_num)

# now assume the input is a list, no string

def filter_list(l): # assume the input is a list
    user_num_list = [] # store the desired integers
    for x in l:
        if isinstance(x, int): # isintance() function that checks if object matches the desired classinfo
            user_num_list.append(x)
    return user_num_list

print(filter_list([1,2,'a',123,'bc']))

# list comprehension example for above

user_num_list = [x for x in l if is_isogram(x,int)]


# use dictionary to count the amount of times something repeats

names = 'calvin,tim,alex,calvin,tim,bob,jones,jones,taylor'
names_split = names.split(',') # my list
names_set = set()

'''
for x in names_split: # this set() stores unique values
    names_set.add(x)
'''
name_dict = dict()

for name in names_split:
    if name in name_dict:
        name_dict[name] += 1 # store the count amount
    else:
        name_dict[name] = 1 # adds it to the dic if not present

print(name_dict)


# to recap - to count amount of times an item displays - just use a list with DICT

# can replace if statement with get() method

name_dict = dict()

for name in names_split:
    name_dict[name] = name_dict.get(name, 0) + 1

print(name_dict)

# reversing integer input exercise *********************

# multiple integers saved into a list

user_input = [2,3,34,345,1,2]
user_input.sort() # call the sort function. the list is now sorted. 
print(user_input) # print the updated list


# single integers seperated into a list
# this method works when the output can be a list

user_input = 123594837 # single line of integers
user_num_list = [int(x) for x in str(user_input)] # str(user_input) turns int into string, then for loop turns it back to integer
user_num_list.sort()
print(type(user_num_list))

# function example for kata
# output needs to be integers

def descinding_order (num):
    user_num_list = [str(x) for x in str(num)] # keep in string format
    user_num_list.sort(reverse=True) # reverse the string list
    sorted_num_str = ''.join(user_num_list) # turn the list into a string
    return int(sorted_num_str) # turn string into integer


# use a txt file to find the store email senders & return sender with highest amount exercise *************
''' -- the second for loop is not necessary, however, 
        if wanted to keep - the x_split[1] needs to ne wrapped another list
email = {}
with open('/Users/calvinpineda/Downloads/mbox-short.txt','r') as file:
    for x in file:
        if x.startswith('From:'):
            non_space = x.strip()
            x_split = non_space.split(':')
            for y in [x_split[1]]: # list wrapped around split list so it can keep only the emails
                email[y] = email.get(y,0) + 1
print(email)
# print(email.items()) # items() is useful with FOR LOOPS        
'''

email = {}
with open('/Users/calvinpineda/Downloads/mbox-short.txt','r') as file:
    for x in file:
        if x.startswith('From:'):
            # non_space = x.strip() # dictionary is stripping, so not necessary
            x_split = x.split(':') # create new list seperating from with the email part
            email[x_split[1].strip()] = email.get(x_split[1].strip(),0) + 1
            # email[x_split[1].strip()] is telling python that the dictionary email, will now have a key
            # key of x_split[1] (is the email part of the split list)
            # = email.get(x_split[1].strip(),0) + 1 is assigning ASSIGNING the value of the key with the get method
            # since its being assigned, it will now be stored in the dictionary
            # and the counter will increase by 1

# cleaned up version
            
email = {}
with open('/Users/calvinpineda/Downloads/mbox-short.txt','r') as file:
    for x in file:
        if x.startswith('From:'):
            x_split = x.split(':')
            email[x_split[1].strip()] = email.get(x_split[1].strip(),0) + 1 # the for loop stores each value into the dictoinary that satisfy the if statement

# acquire max function for dictionary
# use lambda function
max(email, lambda a,b: b) # my version
# correct version
max(email.items(), keys=lambda kv: kv[1]) 
# items() returns keys/values pairs in dictionary
    # keys=lambda kv: kv[1] creating a lambda function, passing a tuple of a keyvalue
        # and returning the value [1] from the tuple (collection of ordered elements), in this case, the key/value pair
# kv is just a varible, it could have been any varible i chose

# store in varible
max_pair = max(email.items(), key=lambda kv: kv[1])

print(max_pair)

# print the max_pair in string format, not tuple format
# learned about format() 
print('{} {}'.format(max_pair[0], max_pair[1]))
# format() replaces the {} within the print quotes
# max_pairs[] are tuples, so i can refernce their position


# mini cup ball PROJECT exercise ***********************************

# three positions: 1, 2, 3
# three moves: A, B, C
# initial position is always 1 
# Moves combination:
    # A swap between 1 & 2
    # b swap between 2 & 3
    # c swap between 1 & 3
# example movement: AB
    # A swaps the ball from 1 to 2
    # next move, B, swaps the ball from 2(current pos) to 3 (final position)

# the only input from user is movement
# how can i move the position of the ball? start by 1. 


ball = [1, 0, 0] # this represent the current position of the ball - ball always starts at 1
# print(ball.index(1))


# as the ball moves, the integer of the ball list updates. 

# the input of ABC, will update the list value

# user input 'A' - code will turn ball[0] = 0, ball[1] = 1/ print current poisition 
# index() function returns the index value where the given element - can be used for current poisition

# lets hard code everything first

# my version but i am stuck

def movement (m): # logic of moving the ball
    if ball.index(1) == 0:
        if m == 'A':
            ball[0] = 0
            ball[1] = 1
        elif m == 'C':
            ball[0] = 0
            ball[2] = 1 
        else:
            return ball.index(1)
    elif ball.index(1) == 1:
        if m == 'B':
            ball[1] = 0
            ball[2] = 1
        else:
            return ball.index(1)
    elif ball.index(1) == 2:
        if m == 'C':
            ball[2] = 0
            ball[0] = 1
        else:
            return ball.index(1)

def game(moves): # accepting the user input
    for m in moves:
        movement(m)
        return ball.index(1)

print(game('AB'))


# ANSWER IF WANTED TO KNOW THE INTERIM POSITION

# Initialize the ball positions
ball = [1, 0, 0]

def swap_positions(pos1, pos2): # 3rd
    # Swap the values at pos1 and pos2 in the ball list
    temp = ball[pos1] # temp = 0
    ball[pos1] = ball[pos2] # ball[pos1] = 1 since ball[pos2] = 1 which is ball[1] = 1
    ball[pos2] = temp # temp = 1

def movement(m): #2nd 
    # Define the moves
    moves = {'A': (0, 1), 'B': (1, 2), 'C': (0, 2)}
    
    # Check if the move is valid
    if m in moves: # 2nd piece of code executed
        # Get the positions to swap
        pos1, pos2 = moves[m] 
        
        # Only perform the swap if the ball is at one of these positions
        if ball[pos1] == 1 or ball[pos2] == 1: # ensure the current ball position is within the letter tuple value
            swap_positions(pos1, pos2)

def game(moves): #1st
    # Perform each move

    for m in moves:
        movement(m) # this is the first excuted peice of code
    
    # Return the final position of the ball
    return ball.index(1) + 1  # Add 1 because positions are 1-based

print(game('AB'))

# IF ONLY INTERESTED IN FINAL POSITION (ORIGINAL ASK)

def game(input_moves):
    # Initialize the ball position
    ball = 1

    # Define the moves
    moves = {'A': (1, 2), 'B': (2, 3), 'C': (1, 3)}

    # Perform each move
    for m in input_moves:
        if m in moves and ball in moves[m]:
            # Update the ball position
            ball = sum(moves[m]) - ball # clever way to find current position of ball

    # Return the final position of the ball
    return ball

print(game('AB'))

# while loops, zip, set, issubset exercise ********************************


# my initial version
'''
yest_list = []
today_list = []

while True:
    try:
        spaces = int(input('amount of parking spaces: '))
        break
    except:
        input('not a number')

yest_spaces = input('enter yesterday parking data: ') # 'C' or '.' where C is parked, '.' is empty

while True:
    try:
        len(yest_spaces) == spaces
        break
    except:
         input('try again')        
            
            
for x in yest_spaces:
    yest_list.append(x)

today_spaces = input('enter todays parking data: ') # 'C' or '.' where C is parked, '.' is empty

while True:
        try:        
            len(today_spaces) == spaces
            break
        except:
            input('try again')


for y in today_spaces:
    today_list.append(y)

# not needed, today_split_list = [w.split('C') for w in today_list]            
            
# OUTPUT: where yest_list[c] == today_list[c]
    # 
counter = 0
for z,h in zip(yest_list, today_list): # zip is used when want to iterate over mutlple sequences (list, strings)
    if z == 'C' and h == 'C':
        counter += 1


print(counter)
'''

'''
# my versions with improvements:
    # just use two while loops


yest_list = []
today_list = []

while True:
    try:
        spaces = int(input('amount of parking spaces: '))
        break
    except:
        input('not a number')

yest_spaces = input('enter yesterday parking data: ') # 'C' or '.' where C is parked, '.' is empty
while yest_spaces != spaces: # while this is correct, it will repeat
    print('invalid input, try again')
    yest_spaces = input('enter yesterday parking data: ') # 'C' or '.' where C is parked, '.' is empty

today_spaces = input('enter todays parking data: ') # 'C' or '.' where C is parked, '.' is empty
while yest_spaces != spaces: # while this is correct, it will repeat
    print('invalid input, try again')
    today_spaces = input('enter todays parking data: ') # 'C' or '.' where C is parked, '.' is empty

for x in yest_spaces:
    yest_list.append(x)

for y in today_spaces:
    today_list.append(y)

counter = 0
for z,h in zip(yest_list, today_list): # zip is used when want to iterate over mutlple sequences (list, strings)
    if z == 'C' and h == 'C':
        counter += 1


print(counter)
'''


# more efficient code
    # no need for list, when zip can run through the strings
    # check if the string only contains 'C' and/or '.'

while True:
    try:
        spaces = int(input('amount of parking spaces: '))
        break
    except:
        input('not a number')

yest_spaces = input('enter yesterday parking data: ') # 'C' or '.' where C is parked, '.' is empty
yest_spaces_upper = yest_spaces.upper()
while len(yest_spaces_upper) != spaces or not set(yest_spaces_upper).issubset({'C', '.'}): # while this is correct, it will repeat - for set, look at chat history
    print('invalid input, try again')
    yest_spaces = input('enter yesterday parking data: ') # 'C' or '.' where C is parked, '.' is empty

today_spaces = input('enter todays parking data: ') # 'C' or '.' where C is parked, '.' is empty
today_spaces_upper = today_spaces.upper()
while len(today_spaces_upper) != spaces or not set(today_spaces_upper).issubset({'C', '.'}): # while this is correct, it will repeat
    print('invalid input, try again')
    today_spaces = input('enter todays parking data: ') # 'C' or '.' where C is parked, '.' is empty


counter = 0
for z,h in zip(yest_spaces, today_spaces): # zip is used when want to iterate over mutlple sequences (list, strings)
    if z == 'C' and h == 'C':
        counter += 1


print(counter)


# finding 2 most common words / tuple, for lopo, items(), sorted exercise *************

# find 2 most common words with romeo txt

common_words = {} # dictionary will store n words and the amount of times they show up
list_words = []
with open('/Users/calvinpineda/Downloads/romeo.txt','r') as file:
    for x in file:
        split_words = x.split()
        for y in split_words:
            common_words[y] = common_words.get(y,0) + 1

# items() is key to getting my desired n common words
for v,w in common_words.items(): # v = key, w = value
    list_words.append((w,v)) # make the value first place, so we can sort by value, paranethesis as its tuple

list_words.sort(reverse=True)
print('{} {}'.format(list_words[0], list_words[1]))


# using a list comprehension

# given common_words{}
print(sorted([(w,v) for v,w in common_words.items()], reverse=True))


# turn string to integer, max/min, test cases

'''high_and_low("1 2 3 4 5")  # return "5 1"
'''

# my initial version

# the input given is strings seperated by a space

# create a split list - sort, by largest, use format print

def high_and_low(num):
    str_num = str(num)
    str_num_split = str_num.split()
    num_list = [int(x) for x in str_num_split] # convert strings to numbers - need to split it first
    num_list.sort(reverse=True)
    high_num = num_list[0]
    num_list.sort(reverse=False)
    low_num = num_list[0]
    result = f"{high_num} {low_num}"
    return result

def test_high_and_low():
    assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
    assert high_and_low("1 -1") == "1 -1"
    assert high_and_low("1 1") == "1 1"
    assert high_and_low("-1 -1") == "-1 -1"
    assert high_and_low("1 -1 0") == "1 -1"
    assert high_and_low("1 1 0") == "1 0"
    assert high_and_low("-1 -1 0") == "0 -1"
    assert high_and_low("42") == "42 42"

test_high_and_low()

# improved version
# dont sort, just use max/min to find highest number/lowest
# no need to turn to integer

def high_and_low(number):
    number_list = number.split()
    high_number = max(number_list, key=int) # converts the list to integer, before finding the max number
    low_number = min(number_list, key=int)
    return f"{high_number} {low_number}"

# string input was given, turn it to an integer because i need to find the high/low
# negative numbers need to be converted to integer so they can be properly assigned a low 


# find specific text, count, dictionary, items(), sorted exercise ***********************

time_dict = {}
with open('/Users/calvinpineda/Downloads/mbox-short.txt','r') as file:
    for x in file:
        if x.startswith('From '):
            words = x.split()
            for word in words:
                if ':' in word: # finding time stamp
                    timestamp = word # storing time stamp by each line
                    time_dict[timestamp[0:2]] = time_dict.get(timestamp[0:2],0) + 1 # storing the first two digit

for hour, dist in sorted(time_dict.items()):
    print(f"{hour} {dist}")
