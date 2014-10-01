#Challenge 15
#Yes, I completed the challenge successfuly. I had a little trouble writing the code to deny access to
#the user if more then 5 attempts are taken. I moved the code around, and wrote and removed a couple
#lines until it worked.


#Inital Values
count = 1
password = "changeme"
enterpass = input("Please enter the password: ")

#Guessing loop
while enterpass != password :
    print("Incorrect. ")
    count = count + 1
    enterpass = input("Please enter the password: ")

    #Security Lockout
    if count > 5 :
        print("Access denied, please press enter to exit and contact secuirty to reset your password. ")
        exit()
        
#If "enterpass" is correct
print("Accepted ")
print("It took you " + str(count) + " tries to enter the correct password. ")

