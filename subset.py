A = set('Rack')
B = set('SuperRack')
C = set('ackR')

print A.union(B) == B and len(A) < len(B) # for B to be strict superset of A.
print A.union(C) == C and len(A) < len(C) # for C to be strict superset of A.