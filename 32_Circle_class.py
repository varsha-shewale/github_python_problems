'''
7.2
Question:
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.

Hints:
Use def methodName(self) to define a method.
'''
import math

class Circle:
    radius = 1
    color = 'transparent'

    def __init__(self, r): #whatever args u specify here should be provided while creating an object of this class
        self.radius = r

    def area(self):
        a = math.pi*self.radius**2
        return a

class ColoredCircle(Circle):
    def __init__(self,r,color):
        self.color = color
        self.radius = r



cir1 = Circle(2)
cir1.radius = 3
a = cir1.area()
print a
print cir1.color

cir2 = Circle(3)
b = cir2.area()
print b

cir3 = Circle(4)
c = cir3.area()
print c

cir4 = ColoredCircle(3,'Dark red')
d = cir4.area()
print d
print cir4.color
