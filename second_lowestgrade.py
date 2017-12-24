'''
find second lowest grade
'''

import operator
def second_lowest():
    f = open('marks.txt','r')
    data = f.read()
    data_list = [x for x in data.split('\r') if x!= ""]

    data_list2d=[]
    for item in data_list:
        data_list2d.append(item.split(','))

    data_list2d = [[name, float(marks)] for name,marks in data_list2d]
    #print data_list2d
    # for item in data_list2d:
    #      item[1] = float(item[1])
    # print data_list2d

    marks = [marks for name,marks in data_list2d]
    sorted_marks = sorted(marks) #ascending order
    second_highest = sorted_marks[1]

    print('\n'.join([name for name,marks in sorted(data_list2d) if marks == second_highest]))

print second_lowest()
