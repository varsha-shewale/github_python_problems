'''
Task
You are given an integer N on one line. The next line contains N space separated integers.
Create a tuple of those N integers. Let's call it T.
Compute hash(T) and print it.

Note: Here, hash() is one of the functions in the __builtins__ module.

Input Format
The first line contains N. The next line contains N space separated integers.

Output Format
Print the computed value.

Sample Input
'''
raw_input()
print hash(tuple(map(int, raw_input().strip().split(" "))))
#3713083796997400956
#3713081631934410656
#3713081631934410656