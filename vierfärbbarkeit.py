import numpy as np
import scipy

n = len(V)

def idx(var, v):
    return var*n + v

c = -np.ones(4*n)
A = []
b = []

# Knotenbeschränkungen
for v in range(n):
    row = np.zeros(4*n)
    row[idx(0, v)] = 1
    row[idx(1, v)] = 1
    row[idx(2, v)] = 1
    row[idx(3, v)] = 1
    A.append(row)
    b.append(1)

# Kantenbeschränkungen
for u, v in E:
    for var in range(4):
        row = np.zeros(4*n)
        row[idx(var, u)] = 1
        row[idx(var, v)] = 1
        A.append(row)
        b.append(1)
result = scipy.optimize.linprog(c, A, b, bounds=(0, 1), integrality=1)
scipy.optimize.linprog(c, A, b, bounds=(0, None), integrality=1)
result.x.reshape(4, n)
