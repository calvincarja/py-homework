
# FINDING THE MOST MENTIONED WORD **************

# varibale
hello = "hello world"
print("%s" % hello)

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

# function example - the varibles are the parameters
def add_numbers(number1, number2):
    result = number1 + number2
    return result

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


# chatGPT alternative code - Advance level code
# code below represents the poem line indent code. for each mentioned position of poemsplit, assing it a number 

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


# function with array for loop
def countbynum (number1, number2):
    countlist = [] # empty list
    for n in range(1, number2 + 1): # range starts at 1, ends at number2 + 1
        countlist.append(n * number1) # append the list with the product of n and number1
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
    if dna: # if dna does not equal ''
        return dna.replace('T', 'U')
    else:
        # Return the empty string directly becuase dna is empty
        return dna

# Example usage
dna_sequence = 'AGTTCTTAAT'  # DNA sequence
rna_sequence = dna_to_rna(dna_sequence)  # RNA sequence
print(f'"{dna_sequence}" => "{rna_sequence}"')



