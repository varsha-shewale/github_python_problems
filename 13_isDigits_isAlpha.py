'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
def count_letter_digits():
    inp = raw_input('Enter sentence ')
    letter = 0
    digits = 0

    for i in inp:
        if i.isalpha() == True:
            letter += 1
        elif i.isdigit() == True:
            digits += 1

    print 'Letters: %d' %letter
    print 'Digits: %d' %digits
    return None

count_letter_digits()

# inp_str = raw_input('Enter words and numbers ')
# li = list(inp_str)
# digits = 0
# letters = 0
#
#
# for item in li:
#     if item.isdigit():
#         digits += 1
#     elif item.isalpha():
#         letters += 1
#
# print ('DIGITS %d' %digits)
# print ('LETTERS %d' %letters)



