'''
Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the first 5 elements in the list.

'''

def square():
    li=[]

    for i in range(1,21):
        li.append(i*i)

    print li[:5]
    print li[-10:-5]
    print li[-5:] # same as [-5:-1] fifth last to last
    print li[5:]

    # Just for another problem to learn converting to Tuple
    t = tuple(li)
    print t[:10] #does not include index 10
    print t[10:]

square()