'''
The challenge is to create a text content analyzer. This is a tool used by writers to find statistics such as word and
sentence count on essays or articles they are writing.
Write a Python program that analyzes input from a file and compiles statistics on it.
The program should output:
1. The total word count
2. The count of unique words
3. The number of sentences
Example output:

Total word count: 468
Unique words: 223
Sentences: 38

Brownie points will be awarded for the following extras:
1. The ability to calculate the average sentence length in words
2. The ability to find often used phrases (a phrase of 3 or more words used over 3 times)
3. A list of words used, in order of descending frequency
4. The ability to accept input from STDIN, or from a file specified on the command line.
This question should be written in Python. Please submit a file (q1.py) with your code.
'''
import re
import operator

#read data from file
fobj = open('input.txt','r')
data = fobj.read()

#Calculate total word count in file
no_period_data = re.sub('.\n', ' ', data)
words = [x for x in no_period_data.split(' ')]
print 'Total word count: %d' %len(words)

#Calculate unique words
unique_words = set(words)
print 'Unique words: %d' %len(unique_words)
#print unique_words
#print words

#Calculate number of sentences in file
no_newline_data = re.sub('\n', ' ', data)
sentences = [x for x in no_newline_data.split('.')]
print 'Sentences: %d' %len(sentences)


#Calculate words per sentence on average
words_in_sentence =[]
len_sentence = []
print sentences
for sentence in sentences:
    words_in_sentence.append(sentence.split(' '))
print words_in_sentence

sum_words = 0
len_sentence = []
for i in words_in_sentence:
    len_sentence.append(len(i))
    sum_words = sum_words + len(i)
#print len_sentence
print 'Average number of words per sentence: %d' %(sum_words/len(sentences))


#for listing words in descending order of frequency
#Dictionary to capture words as keys and frequency as values
freq = {}

for word in words:
    # freq.get() here assigns 0 for initial frequency value of the word and increments it by 1 every time
    freq[word] = freq.get(word,0)+1

sorted_freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True )
print sorted_freq

# for key, value in sorted_freq:
#     print(key, value)
