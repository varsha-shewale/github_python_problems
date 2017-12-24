'''
Question:
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print all strings line by line.

'''

def max_string(stra,strb):

    len1 = len(stra)
    len2 = len(strb)

    if len1>len2:
        print stra
    elif len2>len1:
        print strb
    else:
        print stra +'\n'
        print strb +'\n'

    return None

max_string('I love Data Science1', 'I love Data Science2')

