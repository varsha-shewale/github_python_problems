def count_vowels(s = ''):
    count = 0
    try:
        for item in s.lower():
            if item in 'aeiou':
                count += 1
    except AttributeError:
        return None
    return count

print count_vowels('Asdfdsafdsafds')