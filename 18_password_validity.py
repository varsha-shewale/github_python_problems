'''
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a password and check it according to the above criteria.

Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
import re

p = raw_input('Enter the password ')
print 'password given is %s ' %p
valid_flag = False

if len(p) >=6 and len(p)<=12:
    if re.search('[a-z]',p):
        if re.search('[0-9]',p):
            if re.search('[A-Z]',p):
                if re.search('[$#@]',p):
                    print 'Password is valid'
                    valid_flag = True

if (valid_flag == False):
    print 'Password is invalid. '
