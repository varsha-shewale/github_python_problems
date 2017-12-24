'''
Let's learn about list comprehensions! You are given three integers X,Y and Z representing the dimensions of a cuboid.
You have to print a list of all possible coordinates on a 3D grid where the sum of Xi + Yi + Zi is not equal to N.
If X=2, the possible values of Xi can be 0, 1 and 2. The same applies to Y and Z.

Input Format
Four integers X,Y,Z and N each on four separate lines, respectively.

Output Format
Print the list in lexicographic increasing order.
'''

def cuboid_coord(X,Y,Z,N):
    li = [[x,y,z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if (x+y+z)!=N]
    return li


#print cuboid_coord(1,1,1,2)
print cuboid_coord(2,2,2,2)
