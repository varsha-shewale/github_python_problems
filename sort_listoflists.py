#sort the list of lists below based on ascending number of length of each sublist
import operator

def sort_sublists():
    liofli = [['a','b','c'],['d'],['e','f'],['g','h','i','j','k']]
    out = []
    d = dict()

    for li in liofli:
        d[tuple(li)] = len(li)

    sorted_d = sorted(d.items(),key = operator.itemgetter(1))

    for k,v in sorted_d:
        out.append(list(k))

    return out

print sort_sublists()
