'''
Question:
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.

'''
import math
if True:
    inp_str = raw_input('Enter range for numbers to generate even numbers separated by comma ')
    li = [int(x) for x in inp_str.split(',')]
    #li = int(inp_str.split(',')) #this statement is not correct as int cannot operate on a list.
    #  That's why we iterate through the str elements in above list using list comprehension to
    # convert each str element into int


    a = li[0]
    b = li[1]

    li_num = list(range(a, b+1))
    print li_num
    evenNum = filter(lambda x: x%2 == 0, li_num)
    print evenNum

'''
Question:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
'''
if False:
    li = list(range(1,11))
    m = map(lambda x:x**2,li) #returns a list of squares
    print m

if False:
    li = list(range(1,11))
    add2 = map(lambda x: x+2,li)
    print add2

if False:
    li = list(range(1,11))
    ##map(aFunction, aSequence), filter(aFunction, aSequence), reduce(aFunction, aSequence) take just two args but since
    #pow function takes two arguments below map has three args
    l =map(pow,[2,3,4],[2,3,4])
    print l

if False:
    li = list(range(1,11))
    l = map(lambda x: math.pow(x,2),li)
    print l

if False:
    n = map(None,[1,2,3],[3,5,6])
    print n