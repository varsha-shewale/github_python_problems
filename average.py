import randm as rd

def average():
    #x = rd.sample(range(1,10),5)
    x =[40,20,5]
    if type(x) != list:
        print 'Incorrect'
        return None

    sum = 0
    for num in x:
        sum = sum + num

    avg = sum/len(x)
    print x
    return avg

print average()