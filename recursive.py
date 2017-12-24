def recur_mul(b,p):
    if p == 1:
        return b
    elif p == 0:
        return 1
    else:
        result = b*recur_mul(b,p-1)
        return result

print recur_mul(2,4)