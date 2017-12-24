'''
7.2
Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.

Hints:
Use def methodName(self) to define a method
'''

class Rectangle:

    def __init__(self,l,b):
        self.l = l
        self.b = b

    def areaRect(self):
        a = self.l*self.b
        print a
        return a

r1 = Rectangle(2,4)
r1.areaRect()

