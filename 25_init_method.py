'''
Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
'''

class Animal:
    animal_type = 'Animal'

    def __init__(self, animal_type = None):
        self.animal_type = animal_type



tiger = Animal("Wild")
print '%s animal type is %s' %(Animal.animal_type,tiger.animal_type)

dog =Animal()
dog.animal_type = 'Pet'
print '%s animal type is %s' %(Animal.animal_type, dog.animal_type)


