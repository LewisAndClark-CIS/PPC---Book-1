#! /usr/bin/python3
# Program Name: PPC---Challenge-15.py
# Author:Thomas Morrissey
# Date Written: 9/30/2014

#Pratice Task:
Password = "changeme"
Attempt = input("Enter password: ")
count = 1
while Attempt != Password:
    print("Denied")
    Attempt= input("Enter password: ")
    count += 1
    if count >= 5:
        print("Access denied, please enter to exit and contact security to reset your password")
        exit()
if Attempt == Password:
    print("Accepted")
    print("It took you "+str(count)+" tries!")
#Self-Review
#I have successfully completed the task.
#I did have some Syntax errors.
#I read the code and edit and included the correct punctiation
#i did not find this difficult after Luke helped me with programing.    
          
