#Python Programming Challenges Book 1
#Challenge 13
#Author: Alton Stillwell
#Last Modified: 9/29/2014
#
#print random numbers every three seconds for thirty seconds
###########################
import random
import time
limit = 0
while limit != 33:
    print(random.randint(0,100))
    time.sleep(3)
    limit = limit + 3

#Completed successfully? Yes
#I had lots of errors, time errors and variable errors
#I looked up how to do this kind of thing online, and merged what it was
#showing with my code, and used the limit variable in place of a legit timer
#I found the whole time restriction difficult
