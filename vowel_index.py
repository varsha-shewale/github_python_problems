def vowel_indices(word):
    out =[]
    for index in range(len(word)):
        if word[index].lower() in 'aeiou':
            out.append(index+1)
    return out

print vowel_indices('Mmmm')
