def add_numbers_return_binary1(a,b):
    r = a + b
    r = str(bin(r))
    return r[2:]

def add_numbers_return_binary(a,b):
    return format(a+b,'b')

print add_numbers_return_binary(1,12)