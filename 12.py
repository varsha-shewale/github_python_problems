'''
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

'''

# li = []
# for i in range(1000,3001):
#     if i%2 == 0:
#         li.append(str(i))
#
# print ','.join(li)

# l = [x for x in range(1000,3001) if x%2==0]
# print l

def num_evenDigits():
    li = [x for x in range(200,221) if x%2==0]
    out = []
    print li
    for num in li:
        count = 0
        num_str = str(num)
        digit_li = list(num_str)
        for digit in digit_li:
            if int(digit)%2 == 0:
                count = count + 1
                if count == len(digit_li):
                    out.append(num)

    return out

print num_evenDigits()