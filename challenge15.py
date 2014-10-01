password = 'changeme'
accepted = False
count = 0
attempt =  raw_input('Enter password: ')
while accepted == False:
    if attempt == password:
        print('Accepted')
        count += 1
        print('It took',str(count), 'attempts.')
        accepted = True
    else:
        print('Incorrect password')
        count += 1
        attempt = raw_input('Enter password: ')
        if count >= 5:
            raw_input('Access denied, press enter to exit and contact security to reset your password')
            break
                                                                                
