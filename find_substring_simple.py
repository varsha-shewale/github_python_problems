'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl',
then your program should print

Number of times bob occurs is: 2
'''

def substring_freq(s,subs):
    s = s.lower()
    subs = subs.lower()
    subs_list = []
    count = 0
    for i in range(0, (len(s) - len(subs) + 1)):
        subs_list.append(s[i: i+len(subs)])

    #print subs_list
    count = subs_list.count(subs)
    return count

print substring_freq('azcbobobegghakl','bob')