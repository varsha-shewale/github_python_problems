'''
Let's learn about a new datatype, sets. You are given 2 sets of integers M and N. You have to print their symmetric
difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do
not exist in both.

Input Format
The first line of input contains M. The next line contains M space separated integers. The next line contains N.
The following line contains N space separated integers.

Output Format
Output the symmetric difference integers in ascending order, one per line.

Sample Input
4
2 4 5 9
4
2 4 11 12

Sample Output
5
9
11
12
'''
#Attempt 1------------------
if False:
    li=[]

    for i in range(1,5):
        inp = raw_input()
        if i == 2 or i==4:
            for x in inp.split(' '):
                li.append(int(x))

        i = i+1


    for num in li:
        if li.count(num)>1:
            while li.count(num)>0:
                li.remove(num)

    li.sort()


    for num in li:
        print num
#--------------------------------
if True:
    s1 = set()
    s2 = set()
    for i in range(1,5):
        inp = raw_input()
        if i == 2:
            s1 = set(map(int,inp.split(' ')))
        if i == 4:
            s2 = set(map(int,inp.split(' ')))


    diff = s1.symmetric_difference(s2)

    for num in sorted(list(diff)):
        print num


# for num in li1:
#     if num in lis1.difference(lis2):
#        out.append(num)
# for num in li2:
#     if num in lis2.difference(lis1):
#         out.append(num)
#
# print out.sort()
