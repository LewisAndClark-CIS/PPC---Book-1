import random
rand=(random.randint(0,100))
close = 0
count = 0
while (close<1):
    num=input("Enter a number")
    if int(num)==int(rand):
      print("correct!")
      count=count+1
      close=close+1
    elif int(num)>int(rand):
      print("To high")
      count=count+1
    elif int(num)<int(rand):
      print("To low")
      count=count+1
print(count)
#Done
#invlaid syntex and a int prob
#added a perenthise and declared them all ad int
#all the previouse ones helped
