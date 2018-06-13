import numpy as np
from numpy import dot
from numpy import mat

A = mat([1,2])

B = mat([[1,2], [2,3]])

at = A.T


# print(np.linalg.inv(B))

print(A.reshape(2,1))

# print(dot(A,B))