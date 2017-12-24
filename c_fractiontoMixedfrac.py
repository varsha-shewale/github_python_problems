import fractions
import math

def mixed_fraction(s):
    s1,s2 = s.split('/')
    num,den = int(s1),int(s2)
    signnum,signden = 1,1

    if num < 0:
        signnum = -1
    if den < 0:
        signden = -1
    if den == 0:
        raise ZeroDivisionError

    num = abs(num)
    den = abs(den)

    q,r = divmod(num,den)
    d = den

    g = fractions.gcd(r,d)
    r,d = r/g, d/g
    if r == 0:
        return str(q*signnum*signden)
    elif q == 0:
        return '%d/%d' %(r*signden*signnum,d)
    else:
        return '%d %d/%d' %(q*signnum*signden,r,d)



print mixed_fraction('6011832/-8408661')
