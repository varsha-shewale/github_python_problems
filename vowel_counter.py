 # Paste your code into this box
def vowel_counter(s):
     s = s.lower()
     count = 0
     for i in s:
         if i in ('aeiou'):
             count = count + 1
     return count

print vowel_counter('varsha')