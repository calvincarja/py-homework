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



# approaching above prblem on 1/2/24 

while True:
    user_num = input('enter a number, seperated by a space: ')
    user_num_split = user_num.split()
    if len(user_num_split) != 2:
        print('invalid input. try agin')
        continue
    try:
        user_num_split = [int(x) for x in user_num_split]
        break
    except ValueError:
        print('invalid input, try again')
        continue # keep asking user if valuerror is true
print('your entry is a number, seperated by a space.')

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


# finding 2 most common words / tuple, for lopo, items(), sorted exercise ************* Project idea **

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


# turn string to integer, find max/min, test cases

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



# cipher project pt 1 exercise ********************** project idea **
    

# create dictionary that key represents a letter, and value switches the key (complete)

# {'09': 2, '18': 1, '16': 4, '15': 2, '14': 1, '11': 6, '10': 3, '07': 1, '06': 1, '04': 3, '19': 1, '17': 2}

cipher = {
    'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R',
    'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W',
    'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B',
    'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G',
    'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L',
    'Z': 'M'
}

# user input function
# lets assume no spaces, come back to it later

def machine (word):
    case = word.upper() # turn word upper caps
    switch_word = '' # string that will display new letter combination
    for char in case:
        # switch_word = ''.join(cipher[char]) -- store the value in cipher to string - cipher is already string, thus, can just use +=
        switch_word += cipher[char]
    return switch_word

print(machine('hello'))

# now a version if it contains a space


# create dictionary that key represents a letter, and value switches the key (complete)

# {'09': 2, '18': 1, '16': 4, '15': 2, '14': 1, '11': 6, '10': 3, '07': 1, '06': 1, '04': 3, '19': 1, '17': 2}

cipher = {
    'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R',
    'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W',
    'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B',
    'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G',
    'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L',
    'Z': 'M'
}

# user input function
# lets assume no spaces, come back to it later
# now that it workds, lets handle spaces, keep the space

def machine (word):
    case = word.upper() # turn word upper caps
    split_space = case.split() # this will handle the spaces of the input
    switch_word = '' # string that will display new letter combination
    if len(split_space) > 1: # if input contains multiple words
        for x in split_space: # for loop runs through the list
           switch_word += ' ' # adds a space between the words, not letters
           for y in x: # for loop runs through the letter of each word
           # for y in split_space[x]: incorrect, x, is not an index of split_space list, instead , just use X 
                # switch_word += cipher[y] # add the new arrangement of letters to variable, however, what happens if charcter not in dict?
               switch_word += cipher.get(y,y) # the second y will return y if y not in dictionary
        return switch_word.strip() # all words are added to the varible, and it removes the spaces, before/after
    else:                   
        for char in case:
            switch_word += cipher[char]
        return switch_word

print(machine('hello calvin'))


# advance revised code for exercise above

def machine(word):
    case = word.upper()  # turn word upper caps
    switch_word = ''  # string that will display new letter combination
    
    for char in case:  # for loop runs through each character
        if char != ' ':  # check if the character is not a space, in other words, is a letter?
            switch_word += cipher.get(char, char)  # get the cipher character, or the character itself if it's not in the dictionary
        else: # if char is a space
            switch_word += char  # just add the space to the switch_word
    
    return switch_word


# rollver month data amount exercise ************

# validate each input for data & time is an integer

while True:
    try:
        data = int(input('Enter data plan: '))
        time = int(input('Enter previous time frame: '))
        break
    except:
        print('Not a number. Only numbers please')

# The below approach is incorrect, there is no need to store the values
        # the question is just interested in the remaining amount of data, for N + 1
        # the question is not interested in seeing the values for each iteration
'''
usage_dict = {}
for x in range(0,time):
    usage = int(input(f'Enter amount for month {x}: ')) # amount cannot exceed X, think about later
    usage_dict[x] = usage # this stores the value of usage to the dictionary, this is the first month
    if time - usage != 0:
        remainder = time - usage
        usage_dict[x] = usage + remainder
'''

# my version below was incorrect b/c I was not storing rollver correcly. 
'''

rollover = 0 # this will store the remaining amount
for x in range(0, time): # the plus one, represents the future value, the N + 1
    rollover = rollover + data
    user_input = int(input(f'Enter amount for month {x}: '))
    usage = data - user_input # calculates amount used from data plan
    rollover = data + usage # stores remaining amount

print(rollover)

'''
# correct version

data = int(input('Enter data plan: '))  # Monthly data allowance
time = int(input('Enter previous time frame: '))  # Number of months of data usage provided
rollover = 0  # Initialize the rollover data

for x in range(1, time + 1):  # Start range at 1 to match the month numbers
    user_input = int(input(f'Enter amount for month {x}: '))  # Data used in month x
    rollover = rollover + data - user_input  # Calculate rollover for the next month

# After the loop, rollover contains the unused data that rolls over to month N+1.
# Add the monthly data allowance to the rollover to get the total data for the N+1 month.
next_month_data = rollover + data

print(next_month_data)


# similar problem, for running total exercise **************

'''
Exercise: Savings Account Balance
Background:
Imagine that you have a savings account that accrues interest at the end of each month. The interest is a percentage of the amount of money you have in the account at the end of the month.

Task:
Write a program that calculates the total balance of your savings account after a certain number of months, taking into account monthly deposits, monthly expenses, and interest.

'''

# easy version to ensure I understand what is being asked
# input needed: begining monthly starting balance (complete), monthly expenses (complete), monthly deposit (complete) (job), savings interest, N timeframe

'''
while True:
    try:
        balance = int(input('Enter savings balance: '))
        expenses = int(input('Enter expenses: '))
        deposit = int(input('Enter deposit: '))
        time = int(input('Enter timeframe: '))
        break
    except:
        print('Not a number. Only numbers please')

'''
        
savings_apy = float(0.1) # this is yearly, since N = months, I need to find monthly
monthly_apy = savings_apy / 12 # monthly savings apy

# to find balance, after certain amount of months, that tells me i need a for loop
'''
for x in range(1, time + 1): # so there is no month that starts with 0
    balance = (balance - expenses + deposit) * (1 + monthly_apy) # its my running total
'''

# print(int(balance)) # to remove the decimals

# harder challenge

'''
The initial balance in your savings account.
The monthly interest rate (as a percentage).
The number of months for which the account will be tracked.
A list of tuples where each tuple contains two values: the deposit and the expense for that month.
'''

# the version above wants to introduce varibility (different deposit/expenses amount)

# balance and time can be fixed:


while True:
    try:
        balance = int(input('Enter savings balance: '))
        time = int(input('Enter timeframe: '))
        break
    except:
        print('Not a number. Only numbers please')


# within the time, frame, deposit and expense change
        # thus, the input is asked within the for loop

for x in range(1, time + 1): # so there is no month that starts with 0
    expenses = int(input('Enter expenses for this month: '))
    deposit = int(input('Enter deposit for this month: '))
    print((expenses, deposit))
    balance = (balance - expenses + deposit) * (1 + monthly_apy) # its my running total

print(balance)

# advance print formats for above

while True:
    try:
        balance = int(input('Enter savings balance: '))
        time = int(input('Enter timeframe: '))
        break
    except:
        print('Not a number. Only numbers please')

savings_apy = float(0.1) # this is yearly, since N = months, I need to find monthly
monthly_apy = savings_apy / 12 # monthly savings apy
initial_balance = balance # store initial balance

# within the time, frame, deposit and expense change
        # thus, the input is asked within the for loop

monthly_list = []
for x in range(1, time + 1): # so there is no month that starts with 0
    expenses = int(input('Enter expenses for this month: '))
    deposit = int(input('Enter deposit for this month: '))
    monthly_list.append((expenses, deposit)) # to refence tuple from a list
    balance = (balance - expenses + deposit) * (1 + monthly_apy) # its my running total


print(
   f"initial balance: ${initial_balance}\n" 
   f"monthly interest rate: {monthly_apy*100}% \n"
   f"number of months: {time}\n"
   f"monthly transactions: {monthly_list}\n"
   f"total balance after {time} months: ${round(balance)}\n"
   )

# revised code: initial balance is lost due to me re-initalizing it in the code
# create a stored balance varible 
# for clarity, below is equivilent to my one line of code for a running total
# for financial problems, be careful rounding


for x in range(1, time + 1): # so there is no month that starts with 0
    expenses = int(input('Enter expenses for this month: '))
    deposit = int(input('Enter deposit for this month: '))
    monthly_list.append((expenses, deposit))
    balance += deposit
    balance -= expenses
    balance *= (1 + monthly_apy)


    # saving a password, making it a requirement to contain upper case, exercise **************** Project Idea*


# lets first check if 1 letter is uppercase
    # isupper() is boolean, but all words need to be uppercase
    # we can run a loop, and if three words have true, pass check


# good job - my code is sound and logical
def web_password (password):
    str_password = str(password)
    if not (8 <= len(str_password) <= 12): # validates password length
        return f"incorrect length of password"
    upper_list = []
    for x in password:
        upper_list.append(x.isupper()) # store true value
    if not upper_list.count(True) >= 1:
        return f"Does not include at least one capital letter"
    return f"password saved"

print(web_password('Hello0oo'))

# a clever alternative version below

# instead of list, use a counter variable 
# check if the counter is greater than one, stop the loop
# if counter is less than 1, return password saved message

# i have also update to include lower letter & digit

# if the password meets requriement, pass else, just fail, no need to check again if it fails

def web_password(password):
    str_password = str(password)
    if not (8 <= len(str_password) <= 12):
        return "incorrect length of password"
    upper_count = 0
    lower_count = 0
    digit_count = 0
    for x in password:
        if x.isupper(): 
            upper_count += 1 # adds a 1 to each instance of upper == true
        if x.islower():
            lower_count += 1
        if x.isdigit():
            digit_count += 1
        if upper_count >= 2 and lower_count >= 3 and digit_count >= 1:  # if meets requirement, pass the check. 
            return "password saved" 
    # if upper_count < 2 or lower_count < 3 or digit_count < 1: instead of breaking, I can just pass 
        return "Does not include at least one capital letter"
    # test v4

# quick practice exercise ************
    
# checking if input forms a valid traingle 
    
# given three values represented as lengths of a traingle
# first find s = (a+b+c)/2
# then find area = sqrt[s(s-a)(s-b)(sic)]

def is_triangle(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b) # booleans returning true or false
    



# sorting numbers, summing smallest two
    
    '''
def two_small_numbers (numbers):
    int_list = [str(x) for x in numbers] # for x in numbers is not possible as you cannot iterate over integers
    return int_list
'''

'''
def two_small_numbers (numbers):
    str_num = str(numbers)
    int_list = [int(x) for x in str_num]
    int_list.sort()
    return sum(int_list[0],int_list[1]) # sum function cannot work with two seperate arguments
'''
# the input will be an array
def two_small_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

print(two_small_numbers([4, 9, 7, 1, 2, 4]))


# find language of text

with open('/Users/calvinpineda/Downloads/romeo.txt','r') as file:
    t_count = 0 # enlgish
    s_count = 0 # french
    for line in file:
        line_upper = line.upper()
        t_count += line_upper.count('T')
        s_count += line_upper.count('S')
    print('{} {}'.format(t_count, s_count))
    if t_count >= s_count:
        print('The text is in enlgish')
    else:
        print('The text is in french')


# checking student input to a dictionary, enumarate, all() exercise ******************
        
Letter_list = ['A', 'B', 'C', 'D'] # possible letters to choose from
Answer_bank = {1 : 'B', 2 : 'C', 3 : 'D', 4 : 'A'} # correct answers for each question


# start with non-random input // Simple

# ensure only values from letter_list and commas are inputed // there is an example of exact inputs 
print('Please only enter letters from the following: ', Letter_list)


'''
set().issubset becomes too complicated when using a list of values.
Set.issubset is better to cross refernece if ALL the values match another list, set ect. not a combination


while not set(student_question).issubset({Letter_list}, {','}):
    print('Please only enter letters A, B, C, D')
    student_question = input('Enter the answers for each question, seperated by a comma: ')

    
'''
while True:
    student_question = input('Enter the answers for each question, separated by a comma: ')
    student_question_cap = student_question.upper()
    student_list = student_question_cap.split(',') # list containing the values of student submission

    if all(x in Letter_list for x in student_list): # this is checking if EACH value in input(student_list) IS PRESENT in the letter_list, letter by letter
        break
    else:
        print('Incorrect input, try agian')

correct_answer = 0 # counter for amount of correct submission

'''
my if statment is incorrect - x cannot be the value of student list
AND the key for answer bank


for x in student_list:
    if x == Answer_bank[x]: # cross refernce list to answer bank
        correct_answer += 1
'''

# use enumrate to get allow x, to be the value of student list
# AND be the value of dictionary

for i , x in enumerate(student_list, start=1): # i will be index, x will be value
    if x == Answer_bank[i]: # does the value of student list match the value of answer bank. It is i, as dictionary only refence the values, not the keys
        correct_answer += 1
print(correct_answer)

# cleaner version

Letter_list = ['A', 'B', 'C', 'D'] # possible letters to choose from
Answer_bank = {1 : 'B', 2 : 'C', 3 : 'D', 4 : 'A'} # correct answers for each question


# start with non-random input // Simple

# ensure only values from letter_list and commas are inputed // there is an example of exact inputs 
print('Please only enter letters from the following: ', Letter_list)


while True:
    student_question = input('Enter the answers for each question, separated by a comma: ')
    student_question_cap = student_question.upper()
    student_list = student_question_cap.split(',') # list containing the values of student submission

    # all(list 1, list 2) remeber this if i need to check two lists against each other
    if all(x in Letter_list for x in student_list): # this is checking if EACH value in input(student_list) IS PRESENT in the letter_list, letter by letter
        break
    else:
        print('Incorrect input, try agian')

correct_answer = 0 # counter for amount of correct submission


# use enumrate to get allow x, to be the value of student list
# AND be the value of dictionary

for i , x in enumerate(student_list, start=1): # i will be index, x will be value
    if x == Answer_bank[i]: # does the value of student list match the value of answer bank. It is i, as dictionary only refence the values, not the keys
        correct_answer += 1
print(correct_answer)


# Remove vowels from input exercise *******************

# given an string input, remove
# simple method first - one word only

vowels = ['A', 'E', 'I', 'O', 'U']

'''
def remove_letters (word):
    new_words = ''
    word_upper = word.upper()
    # word_split = word_upper.split()
    for x in word_upper:
        if x not in vowels:
            new_words += x
    return new_words
print(remove_letters('calvinaeiou'))
'''

# multiple words

def remove_letters (word):
    new_words = ''
    word_upper = word.upper()
    word_split = word_upper.split()
    for x in word_split:
        for y in x:
            if y not in vowels:
                new_words += y
        new_words += ' ' # since the input might have multiple words, add a space as the loop runs
    return new_words
print(remove_letters('calvin aeiou'))


# chapter 4 while loops exercise ***************************
'''
    first iteration

def play (myjar, machine1):
    # lets ensure only integers
    if not isinstance(myjar, int) or not isinstance(machine1, int): # 1st check
        raise ValueError("Both inputs must be integers, seperated by a comma")
    # ensure machine1 input only goes up to 35
    if machine1 > 35: # 2nd check
        raise ValueError('second input must be less than / equal to 35')
    if machine1 == 35:
        myjar += 30
    return myjar

print(play(10,35)) # check 30 is added to myjar total
'''



'''
def play (myjar, machine1_placement):
    machine1_payout = 30
    playing_count = 0
    # lets ensure correct inputs
    if not isinstance(myjar, int) or not isinstance(machine1_placement, int): # 1st check
        raise ValueError("Both inputs must be integers, seperated by a comma")
    # ensure machine1 input only goes up to 35
    if machine1_placement > 35: # 2nd check
        raise ValueError('second input must be less than / equal to 35')
    # calculate casino turns
    while myjar > 0:
        if myjar + machine1_placement >= 35: 
            myjar = (myjar - 35) + machine1_payout
            playing_count += 1
        machine1_placement = 0 # this restarts the placment to zero - myjar to last a full cycle
    print('you do not have enough money to play')
    return playing_count

print(play(105,0)) # playing_count should equal 3



# the issue with my code above, was that i was not subtracting myjar to account for the amount of times it takes to reach 35
# i was not running the while loop turn by turn, i was trying to summarize, but within a while loop

def play(myjar, machine1_placement):
    machine1_payout = 30
    playing_count = 0
    plays_since_last_win = machine1_placement  # Track the number of plays since last win
    
    # Ensure correct inputs
    if not isinstance(myjar, int) or not isinstance(machine1_placement, int):
        raise ValueError("Both inputs must be integers, separated by a comma")
    
    # Ensure machine1_placement input is less than 35
    if machine1_placement >= 35:
        raise ValueError('second input must be less than 35')
    
    # Calculate casino turns
    while myjar > 0:
        # Play the machine
        myjar -= 1  # It costs 1 quarter to play - and needs to be tracked turn by turn
        plays_since_last_win += 1  # Increment the counter for plays since last win
        
        # Check for a win
        if plays_since_last_win == 35: # the loop restarts here until plays_since_last_win reaches 35 - then it continues
            myjar += machine1_payout  # Add winnings to myjar
            playing_count += 1  # Increment the number of times played
            plays_since_last_win = 0  # Reset the counter for plays since last win

    return playing_count

print(play(20, 15))
'''
# final part and answer to question
def play(myjar, machine1_placement, machine2_placement, machine3_placement):
    machine1_payout = 30 # every 35th turn
    machine2_payout = 60 # every 100th turn
    machine3_payout = 9 # every 10th turn
    playing_count = 0 # answers the question
    # plays_since_last_win = machine1_placement  # Track the number of plays since last win - i can just pass one varible
    
    # Ensure correct inputs
    if not isinstance(myjar, int) or not isinstance(machine1_placement, int) or not isinstance(machine2_placement, int) or not isinstance(machine3_placement, int):
        raise ValueError("Both inputs must be integers, separated by a comma")
    
    # Ensure machine1_placement input is less than 35
    if machine1_placement >= 35 or machine2_placement >= 100 or machine3_placement >= 10:
        raise ValueError('all inputs must be less than their max amount')
    
    # Calculate casino turns
    while myjar > 0:
        # Play the machine
        myjar -= 3  # It costs 1 quarter to play - and needs to be tracked turn by turn - the admission
        machine1_placement += 1  # Increment the counter for plays since last win - the admission
        machine2_placement += 1
        machine3_placement += 1
        playing_count += 3 # 3 times b/c martha is playing three machines at the same time
        
        # Check for a win
        if machine1_placement == 35: # the loop restarts here until plays_since_last_win reaches 35 - then it continues
            myjar += machine1_payout  # Add winnings to myjar
            machine1_placement = 0  # Reset the counter for plays since last win
        if machine2_placement == 100:
            myjar += machine2_payout
            machine2_placement = 0
        if machine3_placement == 10:
            myjar += machine3_payout
            machine3_placement = 0

    return playing_count

print(play(48, 3, 10, 4))

# cleaned up the code by using a dictonary for the key:value feature

def play(myjar, machine1_placement, machine2_placement, machine3_placement):
    machine_dict = {'machine1': 30, 'machine2': 60, 'machine3': 9} # keys should be fixed, not a varible that gets updated
    playing_count = 0 # answers the question
    # plays_since_last_win = machine1_placement  # Track the number of plays since last win - i can just pass one varible
    
    # Ensure correct inputs
    if not isinstance(myjar, int) or not isinstance(machine1_placement, int) or not isinstance(machine2_placement, int) or not isinstance(machine3_placement, int):
        raise ValueError("Both inputs must be integers, separated by a comma")
    
    # Ensure machine1_placement input is less than 35
    if machine1_placement >= 35 or machine2_placement >= 100 or machine3_placement >= 10:
        raise ValueError('all inputs must be less than their max amount')
    
    # Calculate casino turns
    while myjar > 0:
        # Play the machine
        myjar -= 3  # It costs 1 quarter to play - three machines are played 
        machine1_placement += 1  
        machine2_placement += 1
        machine3_placement += 1
        playing_count += 3 # 3 times b/c martha is playing three machines at the same time
        
        # Check for a win
        if machine1_placement == 35: # the loop restarts here until plays_since_last_win reaches 35 - then it continues
            myjar += machine_dict['machine1']  # Add winnings to myjar
            machine1_placement = 0  # Reset the counter for plays since last win
        if machine2_placement == 100:
            myjar += machine_dict['machine2']
            machine2_placement = 0
        if machine3_placement == 10:
            myjar += machine_dict['machine3']
            machine3_placement = 0

    return playing_count

print(play(48, 3, 10, 4))


# playlist shuffle exercise while loop *************************************

# in order to ensure the input is desired, do not pass a varible. use an input inside the function
# use the function below as the logic function - refernce it in another function
def playlist_logic():
    song_letters = ['A','B','C','D','E']
    while True: 
        keep_playing = input('do you want to shuffle your songs').upper()
        if keep_playing == 'YES':
            button_value = input('enter a number 1 - 3')
            if button_value == '1':
                song_letters.insert(0, song_letters.pop()) # default it pops last place
        
        
playlist_logic()

# final answer

def playlist_logic():
    song_letters = ['A','B','C','D','E']
    while True: 
        keep_playing = input('do you want to shuffle your songs: ').upper()
        if keep_playing == 'YES':
            button_value = input('enter a number 1 - 3: ')
            amount_value = int(input('enter the number of times you want to press that button: ')) # while loop constant
            amount_store = 0 # store inside while loop to reset once user wants to continue shuffling
            while amount_store < amount_value:
                if button_value == '1':
                    song_letters.append(song_letters.pop(0)) # append removes first item, and adds it to the end
                    amount_store += 1 # to keep track of button amount
                elif button_value == '2':
                    song_letters.insert(0, song_letters.pop()) # default pop is last place, thus () is empty - move last item to begin
                    amount_store += 1 # to keep track of button amount
                elif button_value == '3':
                    song_letters.insert(0, song_letters.pop(1)) # swap 2nd item in list with item
                    amount_store += 1 # to keep track of button amount
        else:
            break
    return song_letters
    

# add p to vowels exericse ****************************************************

# a,e,i,o,u vowels

# given an input (store the input), user inserts a 'p' after the vowel
    # then, repeats the vowel 

# example kemija --> kePemiPijaPa

# input will be single line, seperated by a space (space will be the list)

# exercise is indiciating only 1 space, but what if it wants more,
    # do a nested loop to scale the code

def coded_message():
    vowels_list = ['a','e','i','o','u']
    vowel_count = 0
    message = input('enter your message: ')
    message_list = message.split()
    for word in message_list: # runs through every item in the list
        for x in word: # runs through every letter in the word, nested
            if x in vowels_list:
                vowel_count += 1
    return vowel_count

print(coded_message())

# while loop skipping iterations - correct answer for 1 word input


def decode_message(message):
    vowels_list = ['a','e','i','o','u']
    decoded_message = ''
    i = 0
    while i < len(message):
        if message[i] not in vowels_list: #message[i] is the i index
            decoded_message += message[i]
            i += 1 # incrementing the index of i, moves character places
        else:
            decoded_message += message[i]
            i += 3 # thus, here it will skip three places b/c of the fluff two letters 
    return decoded_message

print(decode_message('apapplepe'))


# infection rate exercise *****************************************************************

# p is the threshold for the amount of people infected 750
# R is the amount of people that get infected, only on the next day
# N is the amount of people infected on day 0

# calculate how many days till P is crossed. 

# this is a geometric sequence
 # calculate todays infection, add to the total of yesterday
# day 0 = 1 , day = 5, ratio of infection is 5 per day. 

def infection_rate():
    p = int(input('enter infection threshold: '))
    n = int(input('enter amount of people infected day 0: ')) # represents 1
    r = int(input('the ratio of people infected: '))
    today_infection = 0
    previous_infection = n # day 0
    total_infection = 1 # day 0
    day = 0 # day count - answer output
    while total_infection <= p:
        today_infection = r * previous_infection 
        total_infection =  total_infection + today_infection 
        previous_infection = today_infection 
        day += 1
    return day

print(infection_rate())


# check each boys answer for test exercise ************************************

def correct_answer():
    adriano = ['A','B','C','A','B','C','A','B','C']
    bruno = ['B','A','B','C','B','A','B','C','B']
    goran = ['C','C','A','A','B','B','C','C','A']

    question_amount = int(input('enter amount of questions: '))
    answers = input('enter correct answers: ')

    adriano_correct = 0
    bruno_correct = 0
    goran_correct = 0

    # its not elif b/c we need to grade all the boys answers. so indep if
    # same set up can be used with while loop
    for x in range(question_amount):
        if answers[x] == adriano[x]:
            adriano_correct += 1
        if answers[x] == bruno[x]:
            bruno_correct += 1
        if answers[x] == goran[x]:
            goran_correct += 1
    
    boys_dict = {'adriano': adriano_correct, 'bruno': bruno_correct, 'goran': goran_correct}

    return boys_dict

print(correct_answer())



# web scrapping exercise # 1

with open('/Users/calvinpineda/Downloads/words.txt','r') as file:
    contents = file.read()
    just_words = contents.replace(",","")
    word_list = just_words.split()
    word_dict = {}
    for x in word_list:
        word_dict[x] = word_dict.get(x,0) + 1

    sort_list = sorted(word_dict.items(), key=lambda item: item[1], reverse= True)
print(sort_list[:5])


# using regilar expression and  counter exercise 1
import re
from collections import Counter
with open('/Users/calvinpineda/Downloads/words.txt','r') as file:
    contents = file.read().lower() # ensure all case sensitive is ignored

    words = re.findall(r'\b[a-z]+\b',contents)

    words_freq = Counter(words)

    common_words = words_freq.most_common(5)

    print(common_words)


# web scrapping exercise # 2

# version 1
'''
def exchange (contents,x,y):
    while True:
        if x not in contents:
            x = input('ensure text is present in file: ')
        else:
            break
    replace = contents.replace(x,y)
    return replace

with open('/Users/calvinpineda/Downloads/words.txt','r') as file:
    contents = file.read()

print(contents)
print(exchange(contents,"hello","calvin"))
'''
# version 2
def exchange (contents,x,y):
    if x not in contents:
        return None
    replace = contents.replace(x,y)
    return replace

with open('/Users/calvinpineda/Downloads/words.txt','r') as file:
    contents = file.read()

print(contents)
x = input("entet the text to replace: ")
y = input('enter the text that will take its place: ')

while exchange(contents,x,y) is None:
    print("please ensure the text is in the file")
    x = input("Enter the text to replace: ")

print(exchange(contents,x,y))
