'''
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:
Randomly generate two lists to test this
'''
import randm as rd
a = rd.sample(range(2,20),10)
b =rd.sample(range(1,20),12)
print a,b