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


inp_str = raw_input('Enter comma separated words ')
inp = [x for x in inp_str.split(',')]
# don't do inp = inp.sort() as the sort function does not return anything it just orders list in increasing order
inp.sort()
print ','.join(inp)