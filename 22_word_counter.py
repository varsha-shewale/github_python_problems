'''
Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key
alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''
import operator
inp = raw_input('Enter string ')
freq = {} #created dictionary

for word in inp.split(' '):
    freq[word] = freq.get(word,0)+1 # freq.get() here assigns 0 for initial frequency value of the word and increments it by every time


sorted_freq = sorted(freq.items(),key = operator.itemgetter(0)) #remember to use freq.items()
print sorted_freq

# words = freq.keys()
# words.sort()
# print type(word)
#
# for w in words:
#     print (w +': '+ str(freq[w]))
