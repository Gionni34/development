'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''

# Get input 

email =input("Hello, Please enter you email address: ")


# Clean input/Sanitize

email = email.strip()


# Test 1: It has a "." at the third-to-last index


test_1 = (email[-4] == '.')       # Test true or false
print('Does the email have a  "." at the third to last index?' , test_1)


# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier, email can not be @.com

test_2 = ('@' in email[-6:0:-1])
print('Does the email have exactly one "@" symbol, at the fifth-to-last index or earlier?',test_2 )


# Test 3: There is at least one character before the "@" symbol

test_3 = (email[0] != '@')     # Not equal to
print('Is there at least one character before the "@" symbol?', test_3)


# Test 4: It doesn’t have any spaces (doesn’t contain " ")



# print('Your email does not contain any spaces', test_4)


# Final Test with and Keyword