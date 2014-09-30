#Python Programming Challenges Book 1
#Challenge 15
#Author: Alton Stillwell
#Last Modified: 9/29/2014
#
#password program
###########################
password = "changeme"
guess = ""
attempts = 0
while guess != password:
    guess = input("What is the password? ")
    attempts = attempts + 1
print("Accepted, you guessed", attempts, "times.")
#Completed? Yes
#I had an error where 'changeme' was not defined
#I fixed it by adding quotes around changeme
#I did not find anything difficult
