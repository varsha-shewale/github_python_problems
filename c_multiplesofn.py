def count_by1(x, n):
    out = []
    for item in range(1,n+1):
        out.append(item*x)
    return out

def count_by(x,n):
    return [i*x for i in range(1,n+1)]

print count_by(50,5)
