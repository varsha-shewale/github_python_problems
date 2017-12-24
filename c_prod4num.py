'''
Create a function that returns the lowest product of 4 consecutive numbers in a given string of numbers.

This should only work is the number has 4 digits of more. If not, return "Number is too small".

Example

lowest_product("123456789")--> 24 (1x2x3x4)
lowest_product("35") --> "Number is too small"
'''

def lowest_product(input):
    if len(input) < 4:
        print "Number is too small"
        return None
    inp_li =[]
    inp_str_li = list(input)
    for i in inp_str_li:
        inp_li.append(int(i))
        inp_li.sort()

    for ind in range(3):
        if inp_li[ind+1] - inp_li[ind] > 1:
            print "Numbers should be consecutives"
            return None

    prod = inp_li[0]*inp_li[1]*inp_li[2]*inp_li[3]
    return prod

print lowest_product('1234111')