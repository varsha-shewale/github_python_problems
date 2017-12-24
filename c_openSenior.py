def openOrSenior(data):
    out =[]
    for li in data:
        if li[0] >= 55 and li[1] > 7:
            out.append('Senior')
        else:
            out.append('Open')
    return out

print openOrSenior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]])
