'''
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''

'''
amount = float(0)
inp = raw_input('Enter data for D and W ')
operation = [x for x in inp.split(' ') if x.isalpha() == True]
numbers = [x for x in inp.split(' ') if x.isdigit() == True]

print operation
print numbers

for ind in range(len(operation)):
    if operation[ind] == 'D':
        amount = amount + int(numbers[ind])
    elif operation[ind] == 'W':
        amount = amount - int(numbers[ind])

print 'Amount is %d ' %amount
'''
amount = 0
inp = raw_input('Enter operation and value')
inp_li = [x for x in inp.split(' ')]


for ind in range(len(inp_li)):
    if inp_li[ind] == 'W':
        amount = amount + float(inp_li[ind + 1]) * -1
    elif inp_li[ind] == 'D':
        amount = amount + float(inp_li[ind + 1])

print amount


