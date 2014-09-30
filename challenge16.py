#challenge16
#completed
import random
a = random.randint(1,100)
b = int(input("Guess a number between 1 and 100: "))
tries = 1
while b != a:
    if b < a:
        tries += 1
        b = int(input("Guess higher: "))
    elif b > a:
        tries += 1
        b = int(input("Guess lower: "))

print("Finally you guessed it... ('bout time)...")
print("I almost fell asleep watching you smack a number in", tries, "times to guess", a)
