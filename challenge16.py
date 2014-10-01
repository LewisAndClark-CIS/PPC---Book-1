#challenge16.py
#Karl Pearson
#10/1/14
import random  
number = random.randint(1, 100)
guess = int(input("Guess number: "))
tries = 1
while guess != number:
    if guess < number:
        print("Higher!")
    else:
        print("Lower!")
    tries += 1
    guess = int(input("Guess number: "))
attempt=str(tries)
numberStr=str(number)
print("Nice job! It took you "+attempt+" tries to guess "+numberStr+"!")
#1.yes
#2.I had errors converting the integer to string characters.
#3.I added str commands for the int variables
#4.I found the last print statement difficult becasue of the integers needing to become string characters.

