import numpy as np
import math
m1 = 0.7
m2 = 0.2
m3 = 0.1
data1 = np.array(
    [[0.8*m1, 0.5*m2, 0.2*m3],
     [0.19*m1, 0.3*m2, 0.3*m3],
     [0.01*m1, 0.2*m2, 0.5*m3],
     ])

r1 = 0.6
r2 = 0.3
r3 = 0.1
data2 = np.array(
    [[0.6*r1, 0.7*r2, 0.75*r3],
     [0.3*r1, 0.2*r2, 0.2*r3],
     [0.1*r1, 0.1*r2, 0.05*r3],
     ])


data3 = np.array(
    [[0.85*r1, 0.6*r2, 0.4*r3],
     [0.1*r1, 0.3*r2, 0.3*r3],
     [0.05*r1, 0.1*r2, 0.3*r3],
     ])

mat = data3
row = len(mat)
col = len(mat[0])
mi = 0
for i in range(row):
    for j in range(col):
        mi += (mat[i][j] / sum(sum(mat))) \
              * math.log2((mat[i][j] / sum(sum(mat)))
                          / (mat.sum(axis=1)[j]
                             * mat.sum(axis=0)[i]))
print(mi)
