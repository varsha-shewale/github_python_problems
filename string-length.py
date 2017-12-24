def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    count = 1

    if aStr == "" :
        return 0
    else:
        count = count + lenRecur(aStr[1:])
        return count

print(lenRecur('apple red'))