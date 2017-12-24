
#example anagrams:
# dog, god
# act, cat
# add, dad
# rats, arts

# NOT: art, rats
# NOT: ada, add
# NOT: dog, dog

# Write a function find_anagrams that returns a list of the strings which
# are anagrams of another word in an input list.

#Example:
#find_anagrams(['bat', 'rats', 'god', 'dog', 'cat', 'arts', 'star'])
#=> ['rats', 'god', 'dog', 'arts', 'star']

#get first word from list
#do permutations of the word
#check if the permutations exist in the list
    #if yes then append the word to the output list

import itertools

inp_list = ['bat', 'rats', 'god', 'dog', 'cat', 'arts', 'star']



def find_anagrams(inp_list):
    out=[]
    for word in inp_list:
        perms = [x for x in itertools.permutations(word)]

        perms2=[''.join(x) for x in perms]


        for w in perms2:
            if w in inp_list and w!=word:
                out.append(w)
    return list(set(out))

print find_anagrams(inp_list)
