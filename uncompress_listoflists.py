#Example:
#[[a,a,a,a],[b],[c,c],[a,a],[d],[e,e,e,e]]
#([a,a,a,a,b,c,c,a,a,d,e,e,e,e]).

def unpack():
    liofli = [['a', 'a', 'a', 'a'], ['b'], ['c', 'c'], ['a', 'a'], ['d'], ['e', 'e', 'e', 'e']]
    out =[]
    for li in liofli:
        for element in li:
            out.append(element)
    return out

print unpack()

