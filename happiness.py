import randm

def cal_happiness():
    happiness = 0
    a = [1,2,3,4,5,6]
    print a
    b = [11,12,14,16,15,20]
    print b

    #n = random.sample(xrange(1,20),10)
    n = [1,3,6,6,11,16]
    print n

    for num in n:
        if num in a:
            happiness += 1
        elif num in b:
            happiness -= 1

    return happiness

print cal_happiness()