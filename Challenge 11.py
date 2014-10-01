#Challenge 11
#Yes, Challenge completed successfully. I did not encounter any problems

timeDay=input("On average, in one day, how much time do you spend on a computer? (In hours) ")
if int(timeDay)<2:
    print("That seems reasonable. ")
elif int(timeDay)<4:
    print("Do you have time for anything else? ")
else:
    print("You need to get some fresh air once in a while. And a life. ")
