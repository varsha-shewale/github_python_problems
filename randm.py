import math
def dig_pow(n, p):
    s = str(n)
    dig = list(s)
    sum = 0
    for num in dig:
        sum = sum + int(num)**p
        p += 1

    if sum%n == 0:
        return (sum/n)
    else:
        return -1

print dig_pow(46288,3)