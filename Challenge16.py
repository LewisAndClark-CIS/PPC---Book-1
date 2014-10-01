#Challenge16.py
#By: Karlos Calvillo
#10/1/14
import random

number=random.randint(1, 100)
guess=int(input("Guess number here: "))
tries = 1

while guess != number:
    if guess < number:
        print("Higher")
    else:
        print("Lower")

    tries += 1
    guess = int(input("Guess number here: "))

print("YAY you got it! The right number was", number)
print("It only took you", tries, "tries!\n")

#Response1-Yes
#Response2-No
#Response3-0
#Response4-Nothing
