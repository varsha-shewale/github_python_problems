import numbers

def arr2bin(arr):
    arr_li = list(arr)
    sum = 0
    for num in arr_li:
        if isinstance(num,int) == True:
            sum = sum+num
        else:
            bn = False
            return bn

    bn = bin(sum)
    return bn

print arr2bin([1,10,100,'a'])