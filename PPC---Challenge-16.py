#! usr/bin/python3
# Program Name: PPC---Challegne-1.py
# Author: Thomas Morrissey
# Date: 10/1/2014
import random
the_number = random.randint(0,100)
print("\nI'm thinking of a number between 1 and 100.\n")
guess = int(input("Your Guess: "))
tries = 1
while guess != the_number:
      if guess > the_number:
          print("Lower")
      else:
          print("Higher")
      tries += 1
      guess = int(input("Guess again: "))
if guess == the_number:
    print("Well done! The number was", the_number)
    print("And it only took you", tries, "tires\n")
      
#Self-Review
#I have successfully completed the challenge.
#I ran into multiple errors when I mispelled randint.
#I solved them by asking Brad for help.
#I found this to be midly annoying, but that was mostly my fault.
