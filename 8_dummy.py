'''
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

def word_sort():
    inp = raw_input('Enter comma separated words ')
    inp_li = [x for x in inp.split(',')]
    inp_li.sort()
    return inp_li


w = word_sort()

print ','.join(w)