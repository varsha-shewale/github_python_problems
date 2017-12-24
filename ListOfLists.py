#'Jony,19,Doctor,John,18,Engineer,Nick,25,Architect'
inp = raw_input('Enter name,age,profession ')
a = [x for x in inp.split(',')]
b = list(a)
print len(a)

count = 0

li =[[1 for col in range(0,3)] for row in range(len(a)/3)]
#print li

for row in range(len(a)/3):
    for col in range(3):
        li[row][col] = b[0]
        b.pop(0)

print li
