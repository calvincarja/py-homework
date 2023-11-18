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

