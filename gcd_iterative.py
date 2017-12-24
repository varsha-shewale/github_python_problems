# def gcd(a,b):
#     if a!= 0 and b!=0:
#         s = min(a,b)
#         while s>=1:
#             if a%s==0 and b%s==0:
#                 return s
#             else:
#                 s = s-1
#     elif a == 0:
#         return b
#     elif b == 0:
#         return a
#
#
# print gcd(5,15)

#using Euclid's recurive method for gcd:
def gcdRecur(a,b):
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)

print gcdRecur(18,12)