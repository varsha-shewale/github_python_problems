def flatten(l):
    out = []
    for li in l:
        for item in li:
            out.append(item)
    return out

print flatten([[1,2],[3,4]])