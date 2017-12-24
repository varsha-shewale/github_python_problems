def isPalindrome(inpstr):

    if len(inpstr) <= 1:
        return True

    else:
        return inpstr[0]==inpstr[-1] and isPalindrome(inpstr[1:-1])

def strToChar(inpstr):
    s = inpstr.replace(" ","").lower()
    return s


print isPalindrome(strToChar('Abc cba'))