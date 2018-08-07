target = 66

while True:
    value = input('Enter an integer between 1 and 100: ')
    #print(value)
    try:
        value = int(value)
        #break
    except ValueError:
        print('Enter only integer')
        #continue
    if int(value) > target:
        print(str(value)+ ' is too high')
    elif int(value) < target:
        print('too low')
    else:
        print('Perfect')
