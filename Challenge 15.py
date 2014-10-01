#Challenge 15
#Created by: Zach Golik
count=0
password='changeme'
guess=''

while guess != password:
    guess= input("Please enter password: ")
    count=count+1
else:
    print("Accepted")
    print("It took you "+str(count)+" time(s) to enter your password!")
#Completed successfully? Yes
#Did you have any errors? Yes, the else statement and the while loop
#How did you solve them? I reasearched the problem
#What did you find difficult? Nothing
