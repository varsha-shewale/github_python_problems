'''
Pack consecutive duplicates of list elements into sublists.
If a list contains repeated elements they should be placed in separate sublists.

Example:
?- pack([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [[a,a,a,a],[b],[c,c],[a,a],[d],[e,e,e,e]]
'''

def listoflists():
    li = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
    li_copy = list(li)
    out = []

    count = 1
    for i in range(len(li)-1):
        if li[i] == li[i+1]:
            count += 1
        else:
            out.append(li_copy[:count])
            del li_copy[:count]
            count = 1
    if li_copy != []:
        out.append(li_copy)

    for ind in range(len(out)):
        num = len(out[ind])
        alphabet = out[ind][0]
        out[ind] = []
        out[ind].append (num)
        out[ind].append(alphabet)

    return out

print listoflists()
