'''
Problem Statement

Write a Python script that takes a Scrabble rack as a command-line argument and prints all valid Scrabble words that
can be constructed from that rack, along with their Scrabble scores, sorted by score. An example invocation and output:

$ python scrabble.py ZAEFIEE
17 feeze
17 feaze
16 faze
15 fiz
15 fez
12 zee
12 zea
11 za
6 fie
6 fee
6 fae
5 if
5 fe
5 fa
5 ef
2 ee
2 ea
2 ai
2 ae
'''
import itertools
import operator

f = open('sowpods.txt','r')
data = f.read()

sowpod_words = [x.lower() for x in data.split('\r\n')]
#--------------------------------------
#score dictionary for letters
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

#--------------------------------------
#accept Scrabble rack of 7 letters
rack = raw_input('Enter scrabble rack (7 letters or less, no spaces) ')
if len(rack) == '' or rack.isalpha() != True:
    rack = 'rstlnei'

rack = rack.lower() #lower case
rack = sorted(rack,key = operator.itemgetter(0))#sort alphabetically
rack = ''.join(rack) #join list to form single rack string again
print rack

possible_words =[]

for i in range(1,len(rack)+1):
    for combination in itertools.combinations(rack,i):
        possible_perms = [''.join(x) for x in itertools.permutations(combination)]
        #print possible_perms
        for perm in possible_perms:
            possible_words.append(perm)

unique_words = list(set(possible_words))


valid_words = []

for word in unique_words:
    if word in sowpod_words:
        valid_words.append(word)


print valid_words

points ={}
for word in valid_words:
    total = 0
    for i in range(len(word)):
        total = total + scores[word[i]]
    points[word] = total

#sorting dictionary by values in descending order
sorted_points = sorted(points.items(), key = operator.itemgetter(1),reverse = True)

for k,v in sorted_points:
    print ('%d %s' %(v,k))
