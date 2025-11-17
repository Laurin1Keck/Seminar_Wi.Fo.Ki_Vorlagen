
import numpy as np
import scipy
import itertools

m = 
menge = {i for i in range(m)}
potenzmenge = [set(c) for r in range(len(menge) + 1)
               for c in itertools.combinations(menge, r)]
l = len(potenzmenge)

A = []
b = []

for B in potenzmenge:
    for C in potenzmenge:
        if B < C:
            row = np.zeros(l)
            row[potenzmenge.index(B)] = 1
            row[potenzmenge.index(C)] = 1
            A.append(row)
            b.append(1)

bounds = [(0, None)] * l
c = -np.ones(l, dtype=int)

result = scipy.optimize.linprog(c, A, b, integrality=1)
