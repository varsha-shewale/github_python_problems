'''
1
1*2
1**3
'''

# def pattern1(n):
#     out =['1']
#     out1 =''
#     for i in range(2,n+1):
#         start = '1'
#         pat = start
#         for j in range(1,i):
#             pat = pat + '*'
#         pat = pat + str(i)
#         out.append(pat)
#
#     for item in out:
#         if out[-1] == item:
#             out1 = out1 + item
#         else:
#             out1 = out1 + item + '\n'
#     return out1

def pattern(n):
    s =''
    for i in range(n):
        if i == 0:
            s = '1\n'
        else:
            s += '1{}{}\n' . format('*'*i,i+1)
    return s.rstrip('\n')

print pattern(5)