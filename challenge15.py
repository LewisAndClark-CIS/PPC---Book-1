#challenge15.py
#Karl Pearson
#9/30/14
guess=input('Enter password: ')
tries=1
while guess != 'changeme':
    if guess !='changeme':
        guess=input('Enter password: ')
    tries += 1
    attempt=str(tries)
print('Accepted! It took you '+attempt+' tries.')
    
#1.yes
#2.I had errors because I forgot the colons on the loop
#3.I added the colons to the loop
#4.I found figuring out the while loop difficult at first.
