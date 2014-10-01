######################################################
#Title: ChallengeNo15.py
#Author: Sam Coon
#Date: 9/30/14
######################################################

count = 0
password = 'changeme'
guess=''
while guess != password:
    guess=input("Please enter password: ")
    count=count+1
else:
    print("Accepted!")
    print("It took you " + str(count)+" time(s) to guess your password!")

######################################################
#Self review
#Completed successfully?: Yes 
#Did you have any errors?: Yes
#How did you solve them?: I got help from Zach Golik
#What did you find difficult?: Almost all of it
######################################################
