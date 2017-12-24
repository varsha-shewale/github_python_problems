l1 = [1,2,3,4]
l2 = [3,4,5,6]

copy_l1 = list(l1)

for element in copy_l1:
    if element in l2:
        l1.remove(element)

print l1
print l2