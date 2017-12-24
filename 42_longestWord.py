import re
import numpy as np

#f = open('input.txt','r')
#inp = f.read()
inp = raw_input()

inp_no_period = re.sub('.\r\n',' ',inp)
inp_no_period = re.sub('\.$', '',inp_no_period)

words = [x for x in inp_no_period.split(' ')]
words_len =[len(x) for x in words]

longest_word = ''
for ind in range(len(words_len)):
    if words_len[ind] == max(words_len):
        longest_word = words[ind]

print longest_word
