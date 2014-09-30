#My response: Completed successfully, one error because I put ; instead of :.
#Solved them accordingly, and nothing was difficult. This was the most fun challenge by far.
import random  
number = (random.randint(0,100))
guess = int(input("What number am I thinking of? "))
tries = 1
while guess != number:
    tries += 1
    if guess < number:
        print('Guess higher')
    if guess > number:
        print('Guess Lower')
    guess = int(input('What number am I thinking of? '))
if guess == number:
    print('You guessed correctly!')
    print('It took you '+str(tries)+' tries')
