'''
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other
element of the input tuple is copied, starting with the first one. So if test is the tuple
('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''

# t = (1,2,3)
# print t.index(2)

def altTuples(t):
    nt = tuple()
    #nt =t[::3] #returns (10,13,13)
    #nt =t[1::2] #returns (9,13,18,10)
    nt = t[0::2] #same as t[::2]

    return nt

#print oddTuples((1,2,3,4))
print altTuples((10, 9, 1, 13, 2, 18, 13, 10, 19))