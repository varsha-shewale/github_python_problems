'''
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

'''

'''
li = []
for i in range(2000, 3201, 1):
    if i % 7 == 0 and i % 5 != 0:
       li.append(str(i))

print ', '.join(li)

'''
def div_by7not5():
    num_list = []
    for num in range(2000,3201,1):
        if num%7 == 0 and num%5 != 0:
            num_list.append(str(num))

    return num_list


numbers = div_by7not5()

print ','.join(numbers)