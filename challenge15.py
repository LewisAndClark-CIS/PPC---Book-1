password = ('changeme')
guess = input('Enter the Password... ')
count = 0
while (count <= 5):
    if (count >=5):
        print('Access denied, please press enter to exit and contact security to reset your password')
        break
    if guess == password:
        print('Accepted')
        count = count + 1
        print('It took you', count,'tries.')
        break
    else:
        print('Try again... ')
        count = count + 1

