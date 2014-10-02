Python 3.2.3 (default, Feb 20 2013, 14:44:27) 
[GCC 4.7.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
What's your name?Troy
Hello, Troy
How old are you?17
Traceback (most recent call last):
  File "/home/tscheetner/age.py", line 5, in <module>
    print("So, you're next birthday, you'll be " + new_age)
TypeError: Can't convert 'int' object to str implicitly
>>> ================================ RESTART ================================
>>> 
What's your name? Troy
Hello, Troy
How old are you? 17
So, you're next birthday, you'll be 18
>>> 
>>> #All programs now work successfully.
>>> #I had two errors involving the parenthesis and spacing in the string.
>>> #I edited where parenthesis' needed to be, and added correct spacing.
>>> #Getting the spacing correct.
