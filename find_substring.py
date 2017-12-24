'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring
occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.
Input Format
The first line of input contains the original string. The next line contains the substring.

Each character in the string is an ascii character.

Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input
ABCDCDC
CDC

Sample Output
2
'''

def find_substrings(inp_str):

    substrings =[]
    for i in range(0,len(inp_str)):
        for j in range(1,len(inp_str)+1):
            if i < j:
                substrings.append(inp_str[i:j])
    return substrings

def count_substrings(substrings):
    unique_substrings = list(set(substrings))
    substring_freq ={}

    for word in unique_substrings:
        substring_freq[word] = substrings.count(word)

    return substring_freq

def count_specific_substring():
    inp_str = raw_input('Enter the original string ').lower()
    inp_ss = raw_input('Enter the substring to find its frequency in original string ').lower()

    substrings = find_substrings(inp_str)
    d_freq = count_substrings(substrings)
    #for k,v in d_freq.keys():
    if inp_ss in d_freq.keys() :
        print 'Count of %s in %s is %d' %(inp_ss,inp_str,d_freq[inp_ss])
    else:
        print '%s does not occur in %s ' %(inp_ss,inp_str)
    return None

count_specific_substring()

