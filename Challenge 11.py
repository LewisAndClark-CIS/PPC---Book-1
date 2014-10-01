time=int(input("How long do you spend on a computer per day? "))
if time < 2:
    print("That seems reasonable")
elif time < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get some fresh air once in a while, and a life")
