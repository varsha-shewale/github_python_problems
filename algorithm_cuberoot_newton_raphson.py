'''
The code below uses Newton Raphson approximation.
it says if you make an initial guess g then g - g(x)/g'(x) is a better approximation.
where g(x) is the original equation and g'(x) is its first derivative.

so for squareroot the g(x) will be x**2 - num (where num is the number whose squareroot is am trying to find)
g'(x) will be 2x
for a cuberoot, g(x) will be x**3-num, g'(x) will be 3x**2 here num is number whose cuberoot i want to find.
'''

def find_cuberoot(num):
    g = num/2
    iteration = 0
    epsilon = 0.01

    while abs(g**3 - num) >= epsilon:
        g = g - (g**3-num)/(3.0*g**2)# remember to divide by 3.0 and not 3 to enable float values

        iteration += 1
        print g,
        print iteration
    print 'Iteration %d: %f is a close cuberoot of %f '%(iteration,g,num)

find_cuberoot(126)