import scipy
import itertools
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

n = 4
elements = list(range(1, n + 1))

subsets = []
for r in range(n + 1):
    for comb in itertools.combinations(elements, r):
        subsets.append(frozenset(comb))

m = len(subsets) 

tuples = []
for A in subsets:
    for B in subsets:
        if A < B:
            tuples.append((A, B))

A_list = []
b_list = []

for (A, B) in tuples:
    row = np.zeros(m)

    row[subsets.index(A)] = 1
    row[subsets.index(B)] = 1

    A_list.append(row)
    b_list.append(1)

A_matrix = np.array(A_list)
b_vector = np.array(b_list)

constraints = LinearConstraint(A_matrix, lb=-np.inf, ub=b_vector)

c = -np.ones(m)

bounds = Bounds(lb=np.zeros(m), ub=np.ones(m))
integrality = np.ones(m) 

res = milp(c=c,
           constraints=constraints,
           bounds=bounds,
           integrality=integrality)

print("Status:", res.message)
print("Maximale Größe der Antikette:", -res.fun)

chosen = [subsets[i] for i, val in enumerate(res.x) if val > 0.5]

print("\nAusgewählte Mengen:")
for s in chosen:
    print(set(s))