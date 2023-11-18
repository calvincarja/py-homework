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
