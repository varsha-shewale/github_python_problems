#find anagrams if any in the given list
'''
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
'''
import itertools
def find_anagrams():
    inp_list = ['bat', 'rats', 'god', 'dog', 'cat', 'arts', 'star']
    temp_li =[]
    bool_li = []

    for word in inp_list:
        word_li = list(word)
        word_li.sort()

        new_word = ''
        for l in word_li:
            new_word = new_word + l
        temp_li.append(new_word)

    for word in temp_li:
        if temp_li.count(word) > 1:
            bool_li.append(True)
        else:
            bool_li.append(False)

    return list(itertools.compress(inp_list,bool_li))



print find_anagrams()