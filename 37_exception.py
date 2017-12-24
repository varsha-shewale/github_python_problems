'''
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:
Use try/except to catch exceptions.
'''

def div(num):
    return num/0

try:
    r = div(15)
    print r

except ZeroDivisionError:
    print 'Division by Zero is not allowed '
except Exception, err:
    print 'Caught an exception'
finally:
    print 'This is the final block of code that gets implemented at end of try-except no matter what! '



