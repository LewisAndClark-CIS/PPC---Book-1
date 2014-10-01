import random
tries = 1
the_number=random.randint(1,100)
guess=int(input("Guess a number:"))
while guess != the_number:
    if guess > the_number:
        print("Lower")
    if guess < the_number:
        print("Higher")
    tries += 1
    guess=int(input("Guess again:"))
print("You got it! The number was", the_number)
print("And it took you", tries, "tries!")
