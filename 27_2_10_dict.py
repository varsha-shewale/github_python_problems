'''
Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the
values are square of keys. The function should just print the values only.

'''

def squares():
    dc = {}

    for i in range(1,21):
        dc[i]=i*i

    return dc

d = squares()
#print d

for k, v in d.items():
    print v

