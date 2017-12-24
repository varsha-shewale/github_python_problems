import cmath

def convert_to_polar_coord(x,y):
    p = cmath.phase(complex(x,y)) # calculates angle theta
    r = abs(complex(x,y)) #calculates modulus or r that is distance
    print r,
    print p

convert_to_polar_coord(1,2)