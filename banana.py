def find_substrings(inpstr):
    p1_v_list = ['a','an','ana','anan','anana']
    #p2_c_list = ['b','n','ba','na','ban','nan','bana','nana','banan','banana']
    p2_c_list =['b']

    out =[]
    for i in range(len(inpstr)+1):
        for j in range(1,len(inpstr)+1):
            if i < j:
                out.append(inpstr[i:j])

    v_words = find_vowel_words(out)
    c_words = find_conso_words(out)

    p1_score = 0
    for w in p1_v_list:
        p1_score = p1_score + v_words.count(w)

    p2_score = 0
    for w in p2_c_list:
        p2_score = p2_score + c_words.count(w)

    if p1_score > p2_score:
        print 'Player 1 (who made vowel words) won with score of %d !' %(p1_score)
    elif p1_score < p2_score:
        print 'Player 2 (who made consonant words) won with score of %d !' %(p2_score)
    else:
        print 'Its a tie!'

    return None



def find_vowel_words(inplist):
    vowel_words = []

    for word in inplist:
        if word[0] in 'aeiou':
            vowel_words.append(word)
    return vowel_words

def find_conso_words(inplist):

    conso_words = []
    for word in inplist:
        if word[0] in 'aeiou':
            pass
        else:
            conso_words.append(word)
    return conso_words

find_substrings('banana')
