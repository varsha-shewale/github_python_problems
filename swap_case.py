'''
You are given a string S. Your task is to swap cases. In other words, convert all lowercase letters to uppercase
letters and vice versa.

For Example
Www.HackerRank.com  -> wWW.hACKERrANK.COM
Pythonist 2  -> pYTHONIST 2
'''

def swap_case():
    inp_str = raw_input('Provide string to swap case ')
    inp_list = list(inp_str)
    out = []

    for item in inp_list:
        if item.upper() != item.lower():
            if item.isupper():
                out.append(item.lower())
            else:
                out.append(item.upper())
        else:
            out.append(item)

    swapped = ''.join(out)
    return swapped

print swap_case()