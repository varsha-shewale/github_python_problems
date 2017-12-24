def fibonacci(a,b,c):
    out =[a,b,a+b]
    for i in range(c-3):
        a,b = b,a+b
        sum = a + b
        out.append(sum)
    return out


def tribonacci(signature,n):
    out = list(signature)

    for i in range(n-3):
        out.append(sum(out[-3:]))
    return out


print tribonacci([0,0,1],10)
