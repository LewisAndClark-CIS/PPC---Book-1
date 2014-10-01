#! /usr/bin/python3
# Program Name: Challenge_16.py
# Author: Luke Gosnell
# Date Written: 9/29/2014

#Initialize
import random  
number = (random.randint(0,100))
guess = int(input("What number am I thinking of? "))
tries = 1
while guess != number:
    tries += 1
    if guess < number:
        print("Higher!")
    if guess > number:
        print("Lower!")
    guess = int(input('What number am I thinking of? '))
if guess == number:
    print("Well done!")
    print("It took you '+str(tries)+' tries!")

#Self Review
# Completed successfully
# Syntax error on line 5
# Added lines of code "while guess != number: " and "tries += 1"
# I had trouble and needed help for a lot of this code
