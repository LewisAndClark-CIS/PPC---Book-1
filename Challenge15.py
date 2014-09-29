password="changeme"
count=0
while (count <5):
    passwrd=input("Password")
    if passwrd==password:
        count= count+7
    else:
        print("Wrong")
        count= count+1
if count>=6:
    print("Accepted")
else:
    print("Access denied, please press enter to exit and contact security to reset your password")
    
#yes, finaly!
#didnt know how to make a loop
#i made de loop
#To get the program to repeat
