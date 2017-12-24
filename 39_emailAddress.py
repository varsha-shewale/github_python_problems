'''
Question:

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the
user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
In case of input data being supplied to the question, it should be assumed to be a console input.

Pattern: (d\w+)\W(d\w+)

d        Lowercase letter d.
\w+      One or more word characters.
\W       A non-word character.
'''

import re

em = raw_input('Enter email address ')
pat = "(\w+)@((\w+\.)+(com))"
print pat
result = re.match(pat,em)
print result.group(1)
print result.group(2)
print result.group(3)

'''

emailAddress = raw_input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print r2.group(1)
'''