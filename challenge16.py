import random
number = random.randint(1,10)
count = 0
while True:
    guess = input('Guess what number im thinking of, between 1 and 100.. ')
    if guess == number:
        print('Congratz, you guessed it!')
        count = count + 1
        print('It took you', count,'tries!')
        break
    else:
        print('Guess again!')
        
        
