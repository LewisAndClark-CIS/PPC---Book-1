#Python Programming Challenges Book 1
#Challenge 10
#Author: Alton Stillwell
#Last Modified: 9/29/2014
#
#asks user how long they spend time on a computer
#the responds depending on amount
###########################
time = float(input("How much time do you spend on average on a computer per day? "))
if time <= 0:
    print("Whhaaaaa..?")
elif time < 2:
    print("That seems reasonable")
elif time >= 2:
    print("Get a life")

#Completed successfully? Yes
#I did have some errors,
#i originally reversed the < and > signs by accident
#I solved it by correcting the < and > signs and by adding an < 0 statement
#I didn't really find it difficult, I just messed up the signs a bit..
