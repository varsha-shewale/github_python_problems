'''
Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an
integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''
'''
num = int(raw_input('Enter highest number for squares in dictionary: '))
d = dict()

for i in range(1,num+1,1):
    d[i] = i*i

print d

'''
def squares(num):
    sqr = {}

    for i in range(1,num+1):
        sqr[i]=i*i

    return sqr


s = squares(8)
for k,v in s.iteritems():
    print k,v