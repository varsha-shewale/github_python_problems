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

#take input of 2 digits
inp = raw_input()
inp_list = [int(x) for x in inp.split(',')]

#generate a 2d array
row = inp_list[0]
col = inp_list[1]

arr = [[0 for c in range(col)] for r in range(row)]
#print arr

#ith-jth row = i*j
for r in range(row):
    for c in range(col):
        arr[r][c] = r*c
print arr