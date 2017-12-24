'''
Write a Python script that takes a file containing flash card questions and answers as an argument and quizzes the user
 based on the contents of that file until the user quits the program. Questions should be selected randomly (as opposed
  to going in order through the file), and the user should type in their guess. The script should say whether or not a
  guess is correct and provide the correct answer if an incorrect answer is given.
'''
import randm
import urllib2

def start_quiz(target_url):
    data = urllib2.urlopen(target_url).read()
    #print data
    #f = open('state_capitals.txt', 'r')
    #data = f.read()

    data_list = [x for x in data.split('\n')]
    print data_list

    state_cap = {k:v for k,v in (x.split(',') for x in data_list if x != '')}
    get_questions(state_cap)

def get_questions(state_cap):
    t = True
    while t:

        k = randm.choice(state_cap.keys())
        print k +'?'
        answer = raw_input('Enter your answer ')

        if answer == '' or answer.lower() == 'exit':
            print 'Goodbye! \n'
            t = False
            break
        else:
            if answer.lower() == state_cap[k].lower():
                print 'Correct \n'
            else:
                print 'Wrong. Answer is %s \n' %state_cap[k]


#start_quiz('http://web.mit.edu/jesstess/www/IntermediatePythonWorkshop/metric.txt')
start_quiz('http://web.mit.edu/jesstess/www/IntermediatePythonWorkshop/french_food.txt')