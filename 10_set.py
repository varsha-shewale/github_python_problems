'''
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

# inp_str = raw_input('Enter bunch of words that repeat ')
# li = [x for x in inp_str.split(' ')]
# li_noDup = list(set(li))
# li_noDup.sort()
# print ' '.join(li_noDup)

def words_sort_noDup():
    inp_str = raw_input('Enter comma separated words ')
    inp_li = [x for x in inp_str.split(' ')]

    li_noDup = list(set(inp_li))
    li_noDup.sort()

    return li_noDup

words = words_sort_noDup()
print ' '.join(words)