#My response: Completed successfully, no errors, getting it to ask again was sort of difficult
#I also had trouble finding a fitting exit command so I just used exit()
password = "changeme"
attempt = input('What is the password? ')
count = 1
while attempt != password:
    print('Wrong, please enter again')
    attempt = input('What is the password? ')
    count += 1
    if count >= 5:
        print('Access denied, please press enter to exit and contact security to reset your password')
        exit()
if attempt == password:
    print('Accepted')
    print('It took you '+str(count)+' tries!')
