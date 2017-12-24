def most_frequent(s):
    """Return the most frequently occuring word in s."""
    freq = {}
    # HINT: Use the built-in split() function to transform the string s into an
    #       array
    unordered_words = []
    for word in s.split(" "):
        #freq[word] = freq.get(word,0)+1
        unordered_words.append(word)

    sorted_words = sorted(unordered_words, key = lambda x: x.lower())
    print sorted_words

    for word in sorted_words:
        freq[word] = freq.get(word,0)+1
    print list(freq.keys())

    mx_counts = max(list(freq.values()))
    print mx_counts

    for k,v in freq.iteritems():
        #print k,v
        if v == mx_counts:
            result = k
            break

    return result

if __name__ == '__main__':
    print most_frequent("cat bat mat cat bat cat bat")