'''
Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string,
age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''
'''
from operator import itemgetter

l = []
while True:
    s = raw_input('Enter data and then press enter twice ')
    if not s:
        break
    l.append(tuple(s.split(",")))

print sorted(l, key=itemgetter(0,1,2))
'''
from operator import itemgetter

def sort_tuples():
    li =[]
    while True:
        s = raw_input("enter data, press enter twice once done entering ")
        if not s:
            break
        li.append(tuple(s.split(',')))

    li=sorted(li,key = itemgetter(0,1,2) )
    print li
    return None

sort_tuples()
