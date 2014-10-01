#Challenge15.py
#By: Karlos Calvillo
#9/30/14
password= 'changeme'
attempt=input('Enter password: ')
count = 1
while attempt != password:
    print("Denied")
    attempt=input("Enter password: ")
    count += 1
    if count >= 5:
        print("Access denied, please press enter to exit and contact security to reset your password")
        exit()
if attempt == password:
    print("Accepted")
    print('Accepted, it took you '+str(count)+' tries! ')

#Response1-Yes
#Response2-Yes, I forgot to put certain things in such as count
#Response3-By going back and including it
#Response4-The entire program was fairly difficult
    
