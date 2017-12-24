'''
Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in
[1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
'''

if False:
    li = list(range(1,21))
    evenNumbers = map(lambda x: x**2,filter(lambda x: x%2==0,li))
    print evenNumbers

'''
3.5

Question:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:

Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
'''
if False:
    li = list(range(1,21))
    odd = filter(lambda x: x%2 != 0, li)
    print odd

