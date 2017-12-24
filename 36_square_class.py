'''
7.2
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as
argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:
To override a method in super class, we can define a method with the same name in the super class.
'''

class Shape:
    a = 0
    def __init__(self):
        pass

    def area(self):
        return a


class Square(Shape):
    def __init__(self,l):
        #Shape.__init__(self)
        self.length = l

    def area(self):
        a = self.length**2
        print a
        return a


asquare =Square(3)
asquare.area()
