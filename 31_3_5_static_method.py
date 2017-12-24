'''
7.2
Question:
Define a class named American which has a static method called printNationality.

Hints:
Use @staticmethod decorator to define class static method.
'''

class American():
    id = 'American'
    @staticmethod
    def printNationality():
        print 'American'

class NewYorker(American):
    id = 'American-New Yorker'


am = American()
am.printNationality()
American.printNationality() #no need to create an instance of the class to access a static method

ny = NewYorker()
print ny.id
ny.printNationality() #printNationality is available for NewYorker as it is a child class of American parent class