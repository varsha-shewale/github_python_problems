'''
Create a function that checks if a number is odd.

Expect negative and decimal numbers too. For negative numbers, return true if its absolute value is odd.
For decimal numbers, return true only if the number is equal to its integer part and the integer part is odd.
'''

def is_odd(n):
    if isinstance(n,basestring) == True:
        return False

    n = abs(int(n))
    if n%2 != 0:
        return True
    else:
        return False

print is_odd(-1.218)