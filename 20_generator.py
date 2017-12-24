#divisible by 7

# n = int(raw_input('Enter n '))
#
# def putN(n):
#     i = 0
#     while i<n:
#         if i%7 == 0:
#             yield i
#         i = i + 1
#
# for item in putN(n):
#     print item


def printDiv7(n):
    for i in range(0,n+1):
        if i%7==0:
            print i

printDiv7(22)

