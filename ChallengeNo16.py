######################################################
#Title: ChallengeNo16.py
#Author: Sam Coon
#Date: 10/1/14
######################################################
import random

count = 0
number = random.randint(1,101)
geuss = int(input('Guess the number im thinking of: '))
while geuss != number:
    count = count+1
    if geuss < number:
        print("higher")
    if geuss > number:
        print("lower")
    geuss = int(input("geuss for the number. "))
print("You geussed the number!")
print("It took you " +str(count +1) +" guess(es) to geuss the number!")



    

######################################################
#Self review
#Completed successfully?: Yes
#Did you have any errors?: Yes
#How did you solve them?: I had Brandon and Tyler help me
#What did you find difficult?: Bieng able to keep geussing the number and it telling you lower or higher
######################################################
