import re

def unscramble_eggs(word):
    w = re.sub('egg','',word)
    return w

print unscramble_eggs('FeggUNegg KeggATeggA')