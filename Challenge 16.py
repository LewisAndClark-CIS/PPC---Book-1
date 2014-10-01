#Challenge 16
#Created by: Zach Golik
import random
guess=''
count=0
randomNum=random.randint(1,100)
while guess != randomNum:
    guess=int(input("What number am I thinking of??? "))
    count=count+1
    
    if guess > randomNum:
        print("Lower")
    elif guess < randomNum:
        print("Higher")

print("Well done!")
print("It only took you " +str(count)+" guess(es)!")
#Completed successfully? Yes
#Did you have any errors? Yes, mainly logic errors, but on syntax error
#How did you solve them? Looked them up and had a friend help
#What did you find difficult? Mainly, the if, else statements within the while loop
