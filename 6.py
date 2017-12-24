'''
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''
import math

c = 50
h = 30

inp_str = raw_input('Enter comma separated values for d ')
d = [int(x) for x in inp_str.split(',')] #list comprehension

out = list()
for item in d:
    result = int(math.sqrt(2*c*int(item)/h))
    out.append(str(result))

print ', '.join(out)

