#Python Programming Challenges Book 1
#Challenge 14
#Author: Alton Stillwell
#Last Modified: 9/29/2014
#
#program that prints 1 to 3 w/ a 1 second delay inbetween, then prints 'go!'
###########################
import time
for i in range(1,4):
    print(i)
    time.sleep(1)
print("Go!")
#Completed successfully? Yes
#I had an error where it started at 0 and ended at 2
#I fixed it by changing the parameters in range from (0,3) to (1,4)
#I did not find anything difficult
