'''
Question 7
Level 2
Question
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th
row and j-th column of the array should be i*j
Note: i=0,1.., X-1; j=0,1,...,Y-1
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''

rows = int(raw_input('Enter the # of rows for 2d array '))
cols = int(raw_input('Enter the # of cols for 2d array '))

#creating a 2d array (list of lists) with 0
a2d = [[0 for x in range(cols)] for x in range(rows)]
for r in range(rows):
    for c in range(cols):
        a2d[r][c] = r*c

print a2d
print type(a2d)




