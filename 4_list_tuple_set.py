'''
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

'''



inp = raw_input('Enter bunch of comma separated numbers ')
li = [x for x in inp.split(',') ]
t = tuple(li)
#s = set(t)

print li
print t
print set(t)
