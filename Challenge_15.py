#! /usr/bin/python3
# Program Name: Challenge_15.py
# Author: Luke Gosnell
# Date Written: 9/29/2014

#Initialize
password = "changeme"
attempt = input("Enter Password: ")
count = 1
while attempt != password:
    print("Denied")
    attempt = input('Enter Password: ')
    count += 1
    if count >= 5:
        print("Access denied, please press enter to exit and contact security to reset your password")
        exit()
if attempt == password:
    print('Accepted')
    print('It took you '+str(count)+' tries!')

#Self Review
# Completed successfully
# Syntax error on line 2
# Set count at 1
# my tabbing was off
