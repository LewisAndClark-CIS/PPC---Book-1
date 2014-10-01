#Challenge 16
#Yes, I completed the challenge. I encountered a few errors, mostly just forgetting to convert
#integers to strings, and vice versa. I solved them by using "str()" and "int()" appropriately

import random

#Assigning starting values
count = 1 
ranNumber = (random.randint(0,100)) 

#Opening 
print("I'm thinking of a number between 1 and 100. ")
print("Try to guess what number I'm thinking of. ")

#Users starting guess
guess = int(input("Guess: "))

#What happens if users guess is wrong
while guess != ranNumber :
    if guess > ranNumber :
        print("Wrong. Lower. ")
    elif guess < ranNumber : 
        print("Wrong. Higher. ")

    count = count + 1  #Adding 1, to the amount of tried the users taken
    guess = int(input("Please guess again: "))
    
#What happens if users guess is right 
print("\nWell done! The number was '" + str(ranNumber) + "'. ")
print("It took you " + str(count) + " tries to guess the number. ")
    
