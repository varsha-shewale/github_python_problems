'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

'''

class dummy_str():
    inp_str = ''

    def getString(self):
        self.inp_str = raw_input('Enter a random string ') # as inp_str is a class variable it is prefixed by self.

    def printString(self):
        up = self.inp_str.upper()
        # up is specific to this method and not to the whole class thus we call it without using self.up
        print ('Value of string is %s' %up)

str1 = dummy_str() # created an object or instance of class dummy_str
str1.getString()
str1.printString()


