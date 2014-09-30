#Python Programming Challenges Book 1
#Challenge 16
#Author: Alton Stillwell
#Last Modified: 9/29/2014
#
#guessing game
###########################
import random
number = random.randint(0,100)
guessNum = 0
guess = 101
while guess != number:
    guess = int(input("Enter your guess: "))
    guessNum = guessNum + 1
    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
print("Well done!")
#Completed? YES
#I had an error where i forgot the 'rand' in 'randint',
#and also an error where the variable 'guess' was not defined
#I solved them by ading the 'rand' to the 'int' and by setting the
#guess variable to an impossible number(for the program)
#I didn't find anything really difficult, but I did have to go back
#and check how to make the program produce random numbers
