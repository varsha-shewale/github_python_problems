def checkIfPalindrome(a,b):
    if len(a) == 1 or len(b) == 1:
        return False
    if a == b:
        return False

    a_list = list(a)
    print a_list,

    b_list = list(b)
    b_list.reverse()
    print (b_list)

    if (a_list == b_list):
        return True
    else:
        return False

print checkIfPalindrome('abc','cba')