'''
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''

inp_str = raw_input('Enter some binary numbers separated by comma ')
li = [x for x in inp_str.split(',')]
out = []

for item in li:
    int_item = int(item,2) #convert binary to integer for filtering
    if int_item % 5 == 0:
        out.append(item)

print ', '.join(out)