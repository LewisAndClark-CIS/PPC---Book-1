import random
count = 0
number = random.randint(0,100)
guess = int(input('Guess a number: '))
while guess is not number:
    if guess > number:
        count += 1
        guess = input('Too high, guess again: ')
    else:
        count += 1
        guess = input('Too low, guess again: ')
print('Well done, it took you ' + str(count) + ' tries') 






#Completed: Yes
#Errors: Syntax
#Solved: Added parentheses
#Difficult: None    
