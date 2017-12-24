'''
Let's delve into one of the most basic data types in Python, the list. You are given N numbers. Store them in a list
and find the second largest number.

NOTE: Do not use the insertion sort method.
Input Format
The first line contains N. The second line contains an array A[] of N integers each separated by a space.

Output Format
Output the value of the second largest number.

Sample Input
5
2 3 6 6 5

Sample Output
5
'''

def second_largest_num():
    data = raw_input('Enter a list ')
    li = [int(x) for x in data.split(',')]

    li.remove(max(li))

    return max(li)

print second_largest_num()