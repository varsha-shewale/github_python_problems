'''
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
'''
num = int(raw_input('Enter number for factorial: '))
prod = 1
#
# while (num > 1):
#     prod = num*prod
#     num = num -1

for i in range(1,num+1):
    prod = prod*i
print prod

'''
def factorial(num):
    prod = 1
    for i in range(num,1,-1):
        prod = prod*i
    return prod

print factorial(8)
