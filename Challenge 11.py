#Python Programming Challenges Book 1
#Challenge 11
#Author: Alton Stillwell
#Last Modified: 9/29/2014
#
#same thing as challenge 10 but w/ elif statements
###########################
time = float(input("How long, on average, do you spend on the computer per day, (in hours please): "))
if time < 0:
    print("Skeptical computer is skeptical..")
elif time < 2:
    print("That seems reasonable")
elif time < 4:
    print("Do you have time for anything else?")
elif time <= 24:
    print("You need to get some fresh air once in a while, and a life")
else:
    print("Skeptical computer is skeptical..")
#Completed successfully? Yes
#I did not have any errors
#I used elif and the appropriate < or > signs
#I did not find anything difficult
